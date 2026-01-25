import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time

SCHOOLS_URL = "https://www.sports-reference.com/cfb/schools/"

school_table_cols = {
    "ranker": {
        "ic2_name": "alpha_order",
        "ic2_desc": "Alphabetical order"
    },
    "school_name": {
        "ic2_name": "school_name",
        "ic2_desc": "xxx"
    },
    "year_min": {
        "ic2_name": "year_min",
        "ic2_desc": "xxx"
    },
    "year_max": {
        "ic2_name": "year_max",
        "ic2_desc": "xxx"
    },
    "years": {
        "ic2_name": "total_years",
        "ic2_desc": "xxx"
    },
    "g": {
        "ic2_name": "overall_games",
        "ic2_desc": "xxx"
    },
    "wins": {
        "ic2_name": "overall_wins",
        "ic2_desc": "xxx"
    },
    "losses": {
        "ic2_name": "overall_losses",
        "ic2_desc": "xxx"
    },
    "ties": {
        "ic2_name": "overall_ties",
        "ic2_desc": "xxx"
    },
    "win_loss_pct": {
        "ic2_name": "overall_win_loss_pct",
        "ic2_desc": "xxx"
    },
    "g_post": {
        "ic2_name": "bowl_games",
        "ic2_desc": "xxx"
    },
    "wins_post": {
        "ic2_name": "bowl_games_wins",
        "ic2_desc": "xxx"
    },
    "losses_post": {
        "ic2_name": "bowl_games_losses",
        "ic2_desc": "xxx"
    },
    "ties_post": {
        "ic2_name": "bowl_games_ties",
        "ic2_desc": "xxx"
    },
    "win_loss_pct_post": {
        "ic2_name": "bowl_games_win_loss_pct",
        "ic2_desc": "xxx"
    },
    "srs": {
        "ic2_name": "srs",
        "ic2_desc": "xxx"
    },
    "sos": {
        "ic2_name": "sos",
        "ic2_desc": "xxx"
    },
    "poll_final": {
        "ic2_name": "poll_final",
        "ic2_desc": "xxx"
    },
    "conf_champ_count": {
        "ic2_name": "conf_champ_count",
        "ic2_desc": "xxx"
    },
    "notes": {
        "ic2_name": "notes",
        "ic2_desc": "xxx"
    },
}

# Canonical Sports-Reference keys in desired order
CANONICAL_SR_KEYS = list(school_table_cols.keys())

# Mapping from SR keys -> IC2 column names
IC2_RENAME_MAP = {k: v["ic2_name"] for k, v in school_table_cols.items()}

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Referer": "https://www.sports-reference.com/",
    "Accept-Language": "en-US,en;q=0.9",
}


def get_html(url: str, headers: dict, max_retries: int = 3, backoff: float = 1.5) -> str:
    """Fetch HTML with simple retry/backoff."""
    err = None
    for attempt in range(1, max_retries + 1):
        try:
            r = requests.get(url, headers=headers, timeout=20)
            r.raise_for_status()
            return r.text
        except Exception as e:
            err = e
            if attempt < max_retries:
                time.sleep(backoff ** attempt)
    raise RuntimeError(f"Failed to fetch {url}: {err}")



def parse_header_stats(html):
    soup = BeautifulSoup(html, 'html.parser')

    table = soup.find('table', id='schools')
    if not table:
        raise RuntimeError("Could not find table with id='schools'.")

    thead = table.find('thead')
    if not thead:
        raise RuntimeError('The table does not have a <thead> element.')

    rows = thead.find_all('tr')
    if len(rows) < 2:
        raise RuntimeError('Expected at least two rows in <thead>.')

    second_row = rows[1]
    stats = [th.get('data-stat') for th in second_row.find_all('th')]
    # Remove any None/empty entries
    return [s for s in stats if s]


def parse_school_rows(html: str, expected_stats: list[str] | None = None) -> list[dict]:
    """Parse the schools table body into a list of dicts keyed by data-stat.

    - Uses the header's second-row `data-stat` values as canonical keys when available.
    - Walks all `<tbody>` rows and skips embedded header rows (e.g., `<tr class="thead">`).
    - For each cell, prefers its own `data-stat` attribute for the key; falls back to
      header ordering when needed.
    - Special handling:
      - Do not strip whitespace for the 'notes' column.
      - Extract canonical absolute URL for the school from the 'school_name' cell into 'school_url'.
    """
    soup = BeautifulSoup(html, 'html.parser')

    table = soup.find('table', id='schools')
    if not table:
        raise RuntimeError("Could not find table with id='schools'.")

    # Determine the set/order of keys from the header if not provided
    header_keys = expected_stats or parse_header_stats(html)

    results: list[dict] = []

    tbodies = table.find_all('tbody') or [table]
    for body in tbodies:
        for tr in body.find_all('tr'):
            # Skip embedded header rows commonly marked with class "thead"
            classes = tr.get('class', [])
            if any('thead' in c for c in classes):
                continue

            cells = tr.find_all(['th', 'td'])
            if not cells:
                continue

            row: dict = {}

            # First pass: resolve the intended key for each cell
            for idx, cell in enumerate(cells):
                key = cell.get('data-stat')
                if not key:
                    if idx < len(header_keys):
                        key = header_keys[idx]
                # Compute text with special handling for notes
                if key == 'notes':
                    # Preserve whitespace/newlines exactly as in the cell
                    text = cell.get_text(separator="", strip=False)
                else:
                    text = cell.get_text(strip=True)
                if key:
                    # Assign text value
                    if key not in row:
                        row[key] = text
                    else:
                        row[key] = text  # overwrite if duplicated

                    # If this is the school_name cell, try to extract the URL
                    if key in ('school_name', 'school') and 'school_url' not in row:
                        a = cell.find('a', href=True)
                        if a:
                            href = a.get('href', '') or ''
                            # Make absolute using site base
                            row['school_url'] = urljoin(SCHOOLS_URL, href)
                else:
                    # Unknown key; ignore cell
                    pass

            # Heuristic: require a school identifier to treat as a data row
            if not row.get('school_name') and not row.get('school'):
                continue

            results.append(row)

    return results


if __name__ == '__main__':
    html = get_html(SCHOOLS_URL, HEADERS)

    # Validate header keys (fatal on mismatch)
    parsed_header = parse_header_stats(html)
    if parsed_header != CANONICAL_SR_KEYS:
        raise RuntimeError(
            "Header data-stat list differs from canonical SR keys.\n"
            f"Parsed: {parsed_header}\n"
            f"Expect: {CANONICAL_SR_KEYS}"
        )
    else:
        print('[info] Header data-stat values match canonical keys.')

    # Parse all school rows, skipping embedded header rows
    rows = parse_school_rows(html, expected_stats=CANONICAL_SR_KEYS)

    print(f"[info] Parsed {len(rows)} school rows.")

    # Build a DataFrame from parsed rows
    df = pd.DataFrame(rows)

    # Ensure school_url column exists even if a few rows lacked links
    if 'school_url' not in df.columns:
        df['school_url'] = pd.NA

    # Derive school_key from the last non-empty segment of school_url
    def _extract_school_key(u):
        if not isinstance(u, str) or not u:
            return pd.NA
        try:
            path = urlparse(u).path or ""
            # Remove trailing slash and split
            parts = [p for p in path.split('/') if p]
            return parts[-1] if parts else pd.NA
        except Exception:
            return pd.NA

    df['school_key'] = df['school_url'].map(_extract_school_key)

    # Ensure canonical SR columns exist and order them first
    for col in CANONICAL_SR_KEYS:
        if col not in df.columns:
            df[col] = pd.NA
    extra_cols = [c for c in df.columns if c not in CANONICAL_SR_KEYS]
    df = df[CANONICAL_SR_KEYS + extra_cols]

    # Rename SR columns to IC2 names and reorder (school_url remains as-is)
    df.rename(columns=IC2_RENAME_MAP, inplace=True)
    ic2_cols = [IC2_RENAME_MAP[k] for k in CANONICAL_SR_KEYS]
    # Ensure all ic2 columns exist (in case some were missing earlier)
    for col in ic2_cols:
        if col not in df.columns:
            df[col] = pd.NA
    ic2_extra_cols = [c for c in df.columns if c not in ic2_cols]
    df = df[ic2_cols + ic2_extra_cols]

    # Display a concise preview
    print(f"[info] DataFrame shape: {df.shape}")
    print(df.head(10))

    # Save to CSV in project root
    output_path = "cfb_schools.csv"
    df.to_csv(output_path, index=False, encoding="utf-8")
    print(f"[info] Saved {len(df)} rows to {output_path}")
