import os
import time
import random
from typing import Optional, List
from datetime import datetime
from io import StringIO
import re

import requests
import pandas as pd
from bs4 import BeautifulSoup, Comment

# Reuse cleanup utilities from existing scraper module if available
# try:
#     from sr_schools_scraper import clean_dataframe  # type: ignore
# except Exception:  # Fallback no-op cleaner
#     def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:  # type: ignore
#         return df

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Basic cleanup for Sports-Reference tables:
    - Remove repeated header rows.
    - Strip column labels.
    - Try numeric conversion where sensible.
    """
    # Flatten any MultiIndex columns
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [
            "_".join([str(x) for x in tup if x and str(x) != "nan"]).strip()
            for tup in df.columns
        ]
    else:
        df.columns = [str(c).strip() for c in df.columns]

    # Normalize common SR column-name artifacts like "Unnamed: 1_level_0_"
    cleaned_cols = []
    for c in df.columns:
        s = str(c)
        # Drop prefixes like "Unnamed: 1_level_0_"
        s = re.sub(r"^Unnamed: \d+_level_\d+_", "", s)
        cleaned_cols.append(s)
    df.columns = cleaned_cols

    # Drop rows that are repeated headers
    def is_repeated_header(row):
        matches = 0
        total = 0
        for c, v in row.items():
            if pd.isna(v):
                continue
            total += 1
            if str(v).strip() == str(c).strip():
                matches += 1
        return total > 0 and matches / total > 0.6

    mask = df.apply(is_repeated_header, axis=1)
    df = df.loc[~mask].copy()

    # Trim whitespace
    for c in df.columns:
        if df[c].dtype == object:
            df[c] = df[c].astype(str).str.strip()

    # Attempt numeric conversion for likely numeric columns
    for c in df.columns:
        if df[c].dtype == object:
            # Do not attempt numeric conversion on textual id columns
            lc = str(c).lower()
            if "school" in lc or "url" in lc:
                continue
            ser = pd.to_numeric(df[c].str.replace(",", ""), errors="coerce")
            if ser.notna().mean() >= 0.5:
                df[c] = ser

    df.reset_index(drop=True, inplace=True)
    return df

def _drop_repeated_header_rows(df: pd.DataFrame) -> pd.DataFrame:
    """Remove rows that look like repeated header rows inside <tbody>.
    A row is dropped if the majority of its non-null values equal the column names.
    """
    if df.empty:
        return df
    def is_repeated_header(row: pd.Series) -> bool:
        matches = 0
        total = 0
        for c, v in row.items():
            if pd.isna(v):
                continue
            total += 1
            if str(v).strip() == str(c).strip():
                matches += 1
        return total > 0 and (matches / total) > 0.6
    mask = df.apply(is_repeated_header, axis=1)
    return df.loc[~mask].copy()


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Referer": "https://www.sports-reference.com/",
    "Accept-Language": "en-US,en;q=0.9",
}


def get_html(url: str, headers: dict | None = None, max_retries: int = 3, backoff: float = 1.5) -> str:
    """Fetch HTML with simple retry/backoff."""
    headers = headers or HEADERS
    err: Optional[Exception] = None
    for attempt in range(1, max_retries + 1):
        try:
            r = requests.get(url, headers=headers, timeout=20)
            r.raise_for_status()
            return r.text
        except Exception as e:  # pragma: no cover - network dependent
            err = e
            if attempt < max_retries:
                # exponential backoff
                time.sleep(backoff ** attempt)
    raise RuntimeError(f"Failed to fetch {url}: {err}")


def find_table_by_id(html: str, table_id: str) -> Optional[str]:
    """Return HTML string for <table id=table_id>, searching visible DOM then HTML comments."""
    soup = BeautifulSoup(html, "lxml")

    # 1) Visible DOM first
    tbl = soup.find("table", id=table_id)
    if tbl:
        return str(tbl)

    # 2) Search inside HTML comments (Sports-Reference sometimes comments out tables)
    for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
        frag = BeautifulSoup(comment, "lxml")
        tbl = frag.find("table", id=table_id)
        if tbl:
            return str(tbl)

    return None


def _manual_parse_table(table_html: str) -> pd.DataFrame:
    """Very small manual parser for a single table HTML string when read_html fails.

    - Extract header cells from last <tr> in <thead>, or first non-empty row in <tbody>.
    - Build rows from <tbody>, skipping <tr class="thead">.
    """
    soup = BeautifulSoup(table_html, "lxml")
    table = soup.find("table") or soup

    # Headers
    headers: List[str] = []
    thead = table.find("thead")
    if thead:
        head_rows = thead.find_all("tr")
        if head_rows:
            last = head_rows[-1]
            headers = [th.get_text(strip=True) for th in last.find_all(["th", "td"])]
    if not headers:
        # Fallback: use first body row that looks like header-ish
        body = table.find("tbody") or table
        for tr in body.find_all("tr"):
            cls = tr.get("class", [])
            if any("thead" in c for c in cls):
                continue
            cells = tr.find_all(["th", "td"])
            if not cells:
                continue
            headers = [c.get_text(strip=True) for c in cells]
            break

    rows: List[List[str]] = []
    bodies = table.find_all("tbody") or [table]
    for body in bodies:
        for tr in body.find_all("tr"):
            cls = tr.get("class", [])
            if any("thead" in c for c in cls):
                continue
            cells = tr.find_all(["td", "th"])
            if not cells:
                continue
            vals = [c.get_text(strip=True) for c in cells]
            if any(v.strip() for v in vals):
                rows.append(vals)

    # Normalize rectangular shape
    max_len = max([len(headers)] + [len(r) for r in rows] or [0])
    if headers and len(headers) < max_len:
        headers = headers + [f"col_{i}" for i in range(len(headers), max_len)]
    norm_rows = [r + ["" for _ in range(len(r), max_len)] for r in rows]

    if not headers:
        # generate generic headers
        headers = [f"col_{i}" for i in range(max_len)]

    df = pd.DataFrame(norm_rows, columns=headers)
    return df


def parse_table_html(table_html: str) -> pd.DataFrame:
    """Parse a single table HTML string into a cleaned DataFrame.

    Pre-clean step removes embedded header rows (<tr class="thead">) from <tbody>
    before handing HTML to pandas, then applies standard cleaning and a
    header-row heuristic drop as a safety net.
    """
    # Pre-clean: remove embedded header rows from the HTML itself
    soup = BeautifulSoup(table_html, "lxml")
    table = soup.find("table") or soup
    bodies = table.find_all("tbody") or [table]
    for body in bodies:
        for tr in body.find_all("tr"):
            cls = tr.get("class", [])
            if any("thead" in c for c in cls):
                tr.decompose()
    cleaned_html = str(table)

    df: pd.DataFrame
    try:
        dfs = pd.read_html(StringIO(cleaned_html))  # wrap literal HTML to avoid FutureWarning
        if isinstance(dfs, list) and len(dfs) > 0:
            # pick the largest by row count
            df = max(dfs, key=lambda d: len(d))
        else:
            df = pd.DataFrame()
    except Exception:
        df = pd.DataFrame()

    if df.empty:
        # Fall back to manual parser on the pre-cleaned HTML
        df = _manual_parse_table(cleaned_html)

    df = clean_dataframe(df)
    # Ensure no embedded header rows from <tbody>
    df = _drop_repeated_header_rows(df)

    # Extra guard: drop any rows where majority of non-null values equal column names
    if not df.empty:
        def _is_repeated_header(row: pd.Series) -> bool:
            matches = 0
            total = 0
            for c, v in row.items():
                if pd.isna(v):
                    continue
                total += 1
                if str(v).strip() == str(c).strip():
                    matches += 1
            return total > 0 and (matches / total) > 0.6
        mask = df.apply(_is_repeated_header, axis=1)
        if mask.any():
            df = df.loc[~mask].copy()
    return df


def main():
    input_csv = "cfb_schools.csv"
    output_csv = "cfb_school_tables.csv"
    failures_csv = "cfb_school_tables_failures.csv"

    if not os.path.exists(input_csv):
        raise RuntimeError(f"Input file not found: {input_csv}")

    schools_df = pd.read_csv(input_csv)

    required = {"school_key", "school_url"}
    if not required.issubset(set(schools_df.columns)):
        raise RuntimeError(
            f"{input_csv} must include columns: {sorted(required)}. Found: {list(schools_df.columns)}"
        )

    results: List[pd.DataFrame] = []
    failures: List[dict] = []

    total = len(schools_df)
    print(f"[info] Processing {total} schools from {input_csv} ...")

    for idx, row in schools_df.iterrows():
        school_key = str(row.get("school_key", "")).strip()
        school_url = str(row.get("school_url", "")).strip()
        if not school_key or not school_url:
            failures.append({"school_key": school_key, "school_url": school_url, "error": "missing key/url"})
            continue

        try:
            html = get_html(school_url, HEADERS)
            table_html = find_table_by_id(html, school_key)
            if not table_html:
                raise RuntimeError(f"table id='{school_key}' not found (visible or commented)")

            df = parse_table_html(table_html)
            if df.empty:
                raise RuntimeError("parsed empty table")

            # Attach metadata
            extracted_at = datetime.now().isoformat(timespec='seconds')
            df["school_key"] = school_key
            df["school_url"] = school_url
            df["extracted_at"] = extracted_at

            results.append(df)
            print(f"[ok] {idx+1}/{total} {school_key}: rows={len(df)}")
        except Exception as e:
            failures.append({"school_key": school_key, "school_url": school_url, "error": str(e)})
            print(f"[fail] {idx+1}/{total} {school_key}: {e}")
        # Be polite to the site
        time.sleep(0.5 + random.random() * 0.5)

    if results:
        combined = pd.concat(results, ignore_index=True, sort=False)
        # Fill NaNs with empty strings as requested
        combined = combined.fillna("")
        # Also normalize common textual null markers in object columns
        obj_cols = combined.select_dtypes(include=["object"]).columns
        if len(obj_cols) > 0:
            null_tokens_re = re.compile(r"^(nan|none|null|na|n/a)$", re.IGNORECASE)
            for col in obj_cols:
                # ensure string dtype for replace, but keep empty strings empty
                combined[col] = (
                    combined[col]
                    .astype(str)
                    .str.strip()
                    .str.replace(null_tokens_re, "", regex=True)
                )
        # Safety net: ensure no NaNs remain
        combined = combined.fillna("")
        # Small preview to verify new columns exist
        try:
            print(combined[["school_key", "school_url", "extracted_at"]].head())
        except Exception:
            pass
        combined.to_csv(output_csv, index=False, encoding="utf-8")
        print(f"[info] Saved combined table rows: {len(combined)} -> {output_csv}")
    else:
        print("[warn] No successful tables parsed; no output CSV written.")

    if failures:
        pd.DataFrame(failures).to_csv(failures_csv, index=False, encoding="utf-8")
        print(f"[info] Saved failures report: {failures_csv} ({len(failures)} failures)")

    print(
        f"[summary] processed={total} ok={len(results)} failed={len(failures)} | output={output_csv}"
    )


if __name__ == "__main__":
    main()
