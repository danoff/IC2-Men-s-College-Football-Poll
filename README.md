# IC² Men's College Football Poll

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/pandas-1.5%2B-orange)](https://pandas.pydata.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0%2B-green)](https://scikit-learn.org/)
[![License: MPL 2.0](https://img.shields.io/badge/License-MPL_2.0-brightgreen.svg)](https://opensource.org/licenses/MPL-2.0)
[![Notebooks](https://img.shields.io/badge/notebooks-Jupyter-orange)](https://github.com/danoff/IC2-Men-s-College-Football-Poll/tree/main/notebooks)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![Last Updated](https://img.shields.io/badge/updated-December%202025-blue)]()
[![GitHub Issues](https://img.shields.io/github/issues/danoff/IC2-Men-s-College-Football-Poll)](https://github.com/danoff/IC2-Men-s-College-Football-Poll/issues)
[![GitHub Stars](https://img.shields.io/github/stars/danoff/IC2-Men-s-College-Football-Poll)](https://github.com/danoff/IC2-Men-s-College-Football-Poll/stargazers)

**A [CFP](https://en.wikipedia.org/wiki/College_Football_Playoff)-Era Statistical Ranking System with 80% Championship Prediction Accuracy**

This is an open-source men's American/gridiron college football 🏈 poll that provides quantitative rankings based on championship teams from the College Football Playoff era (2014–Present). This was made by Charles Jeffrey Danoff, Isaih Battiste, and Chris Hanes.

## Revised Poll for Semifinals (January 8th, 2026 Update)

Ahead of the semifinal games that start tonight we have a revised poll! In addition to an [updated python Jupyter notebook](https://github.com/danoff/IC2-Men-s-College-Football-Poll/blob/main/IC2%20Open%20Source%20College%20Football%20Poll%207%20January%202026%20for%20GitHub.ipynb), we also made the [data set](https://github.com/danoff/IC2-Men-s-College-Football-Poll/blob/main/cfb_school_tables_2026-01-02v1.csv) avaialble for the first time if you want to run the model on your own!

Results are through January 1st, 2026, so they do not include games on the 2nd. It is safe to assume Navy would be higher than 31st [following their win](https://www.sports-reference.com/cfb/boxscores/2026-01-02-cincinnati.html).

### Full Top 35 Comparison Table

| IC² Rank | Team | Win% | SRS | SOS | IC² Score | CFP Seed | Difference | Made Playoff? | Alive in Playoff? |
|:--------:|:-----|:----:|:---:|:---:|:---------:|:--------:|:----------:|:-------------:|:-----------------:|
| 1 | Indiana | 1.000 | 24.05 | 5.48 | 97.7 | 1 | 0 | ✅ Yes | ✅ Yes (Final 4) |
| 2 | Oregon | 0.929 | 22.04 | 5.97 | 92.8 | 5 | +3 | ✅ Yes | ✅ Yes (Final 4) |
| 3 | Ohio State | 0.857 | 23.03 | 6.18 | 87.5 | 2 | -1 | ✅ Yes | ❌ No (Lost to Miami) |
| 4 | Miami (FL) | 0.857 | 20.36 | 6.29 | 79.9 | 10 | +6 | ✅ Yes | ✅ Yes (Final 4) |
| 5 | Notre Dame | 0.833 | 21.73 | 5.23 | 76.3 | — | — | ❌ **No** | — |
| 6 | Texas Tech | 0.857 | 21.56 | 3.34 | 73.7 | 4 | -2 | ✅ Yes | ❌ No (Lost to Oregon) |
| 7 | Ole Miss | 0.929 | 16.56 | 3.99 | 71.9 | 6 | -1 | ✅ Yes | ✅ Yes (Final 4) |
| 8 | Texas A&M | 0.846 | 17.77 | 5.54 | 62.7 | 7 | -1 | ✅ Yes | ❌ No (Lost to Miami) |
| 9 | BYU | 0.857 | 16.09 | 6.45 | 61.6 | — | — | ❌ No | — |
| 10 | Georgia | 0.857 | 17.50 | 4.57 | 59.7 | 3 | -7 | ✅ Yes | ❌ No (Lost to Ole Miss) |
| 11 | Utah | 0.846 | 17.99 | 2.60 | 48.9 | — | — | ❌ No | — |
| 12 | Alabama | 0.733 | 13.29 | 7.42 | 19.0 | 9 | -3 | ✅ Yes | ❌ No (Lost to Indiana) |
| 13 | Oklahoma | 0.769 | 13.28 | 5.13 | 18.4 | 8 | -5 | ✅ Yes | ❌ No (Lost to Alabama) |
| 14 | Vanderbilt | 0.769 | 14.75 | 3.06 | 16.8 | — | — | ❌ No | — |
| 15 | Texas | 0.769 | 12.64 | 4.72 | 15.2 | — | — | ❌ No | — |
| 16 | USC | 0.692 | 14.88 | 6.34 | 13.9 | — | — | ❌ No | — |
| 17 | Iowa | 0.692 | 13.99 | 4.53 | 8.4 | — | — | ❌ No | — |
| 18 | Arizona | 0.750 | 12.47 | 2.55 | 8.0 | — | — | ❌ No | — |
| 19 | Illinois | 0.692 | 11.74 | 6.13 | 7.2 | — | — | ❌ No | — |
| 20 | Virginia | 0.786 | 10.93 | 1.36 | 7.0 | — | — | ❌ No | — |
| 21 | James Madison | 0.857 | 10.60 | -2.55 | 6.8 | 12 | -9 | ✅ Yes | ❌ No (Lost to Oregon) |
| 22 | Michigan | 0.692 | 11.11 | 5.96 | 6.1 | — | — | ❌ No | — |
| 23 | North Texas | 0.857 | 10.01 | -2.85 | 5.7 | — | — | ❌ No | — |
| 24 | Washington | 0.692 | 13.14 | 3.45 | 5.7 | — | — | ❌ No | — |
| 25 | TCU | 0.692 | 9.48 | 4.17 | 3.0 | — | — | ❌ No | — |
| 26 | Tulane | 0.786 | 6.75 | 1.46 | 3.0 | 11 | -15 | ✅ Yes | ❌ No (Lost to Ole Miss) |
| 27 | Houston | 0.769 | 7.79 | 1.02 | 2.8 | — | — | ❌ No | — |
| 28 | Louisville | 0.692 | 9.19 | 2.50 | 2.0 | — | — | ❌ No | — |
| 29 | Iowa State | 0.667 | 9.46 | 3.46 | 1.9 | — | — | ❌ No | — |
| 30 | Georgia Tech | 0.692 | 8.45 | 2.22 | 1.6 | — | — | ❌ No | — |
| 31 | Navy | 0.833 | 4.50 | -1.84 | 1.6 | — | — | ❌ No | — |
| 32 | SMU | 0.667 | 10.44 | 1.03 | 1.5 | — | — | ❌ No | — |
| 33 | South Florida | 0.692 | 10.63 | -0.68 | 1.4 | — | — | ❌ No | — |
| 34 | NC State | 0.615 | 8.01 | 5.63 | 1.2 | — | — | ❌ No | — |
| 35 | Arizona State | 0.615 | 8.07 | 5.38 | 1.1 | — | — | ❌ No | — |

## Community

Read more details and join the community discussion!

12/30/2025
- Posted [new ranking on Bluesky](https://bsky.app/profile/teachinglaboratory.bsky.social/post/3mbb2ixk4dk2s) ahead of quarterfinal

12/23/2025
- Tweeted about [revised poll](https://x.com/fireballfinds/status/2003499507779289422)

12/22/2025
- Posted [Revised Rankings for IC² Open Source Men's College 🏈 Poll following first weekend of CFP!](https://www.reddit.com/r/sportsanalytics/comments/1ptfyjm/revised_rankings_for_ic%C2%B2_open_source_mens_college/) on Reddit

12/19/2025
- Posted [New Rankings for IC² Open Source Men's College 🏈 Poll!](https://www.reddit.com/r/sportsanalytics/comments/1pqn81j/new_rankings_for_ic²_open_source_mens_college_poll/) on Reddit 

12/06/2025 
- Described results and methodology LinkedIn [article](https://www.linkedin.com/pulse/new-open-source-poll-mens-college-football-surcc) ·
- Shared results on [Twitter/X](https://x.com/FireballFinds/status/1997338915926094094)

12/05/2025 
- Announced primary results Reddit [Post](https://www.reddit.com/r/sportsanalytics/comments/1pfbvmj/) ·

09/30/2025
- Exploratory Reddit [Post](https://www.reddit.com/r/fsusports/comments/1nuq43v/new_homemade_computer_ranking_system/)

11/20/2024 
- Inspiration on [Twitter/X](https://x.com/FireballFinds/status/1859242094570701154)

## Methodology

### Training Approach
- **Training period**: 2014-2024 (CFP era only)
- **Training set**: 1,566 team-seasons, 11 champions
- **Validation**: 2014-2023 (excluding 2024 from validation)

### Model Features
The IC² Poll uses only three statistical features:
1. **Win Percentage** (`Overall_Pct`): Game winning percentage
2. **SRS Rating** (`SRS_SRS`): Simple Rating System (team strength)
3. **Strength of Schedule** (`SRS_SOS`): Opponent difficulty

### Champion Criteria
Based on analysis of 2014-2024 champions:
1. Win Percentage ≥ 87.5%    (max 1-2 losses)
2. Simple Rating System (SRS) ≥ 20.1      (elite team quality)
3. Strength of Schedule (SOS) ≥ 5.2       (tough schedule)

### Methodological Strengths
1. **Modern relevance**: CFP-era training only
2. **Statistical purity**: No poll influence
3. **Transparency**: Three simple, interpretable features
4. **Actionable insights**: Champion criteria provide clear benchmarks

### **Model**

* Logistic Regression (balanced class weighting)
* StandardScaler
* 80% validation accuracy

### **Model Implementation**
- **Algorithm**: Logistic Regression with class weighting
- **Scaling**: StandardScaler for feature normalization
- **Validation**: 80% accuracy on 2014-2023 champions

## Results Interpretation

### 📈 Historical Performance **Accuracy (2014-2023)**
- **80% accuracy** (8/10 champions correctly predicted)
- **Correct predictions**: 2014, 2015, 2018, 2019, 2020, 2021, 2022, 2023
- **Missed**: 2016 (predicted Alabama, actual Clemson), 2017 (predicted Wisconsin, actual Alabama)

### **IC² Score (0-100)**
* **90+**: Elite championship contender
* **80–89**: Playoff caliber
* **70–79**: Fringe contender
* **<60**: Not championship caliber

### **Champion Profile Score (0-3)**
- **3**: Perfect champion profile (historically wins 90%+)
- **2**: Near-complete profile (true contender)
- **1**: One-dimensional team
- **0**: Not championship caliber

### **Team Assessment Categories**
- **Complete Contender**: Meets all 3 champion criteria
- **Strong Contender**: Meets 2/3 criteria  
- **One-Dimensional**: Meets 1/3 criteria
- **Long Shot**: Meets 0/3 criteria

### 🤔 Why IC²?

Traditional polls suffer from:
- **Recency bias**: Overreacting to last week's results
- **Brand bias**: Blue bloods get benefit of doubt
- **Inconsistent criteria**: Different voters value different things
- **Subjectivity**: No transparency in decision-making

#### **IC² fixes this by:**
- ✅ Using only objective performance metrics
- ✅ Training on actual CFP champion data (2014-2024)
- ✅ Providing transparent, reproducible rankings
- ✅ Achieving 80% historical accuracy
- ✅ Zero poll influence

### 📊 **2025 Rankings (Top 10)**

*Last updated: December 6, 2025*
⚠️ = Strong Contender (meets 2/3 champion criteria)

| Rank | Team       |  Win% |  SRS  |  SOS | IC² Score | Profile |
| :--: | :--------- | :---: | :---: | :--: | :-------: | :-----: |
|   1  | Ohio State | 1.000 | 24.27 | 3.19 |   96.13   |  2/3 ⚠️ |
|   2  | Indiana    | 1.000 | 21.99 | 2.91 |   93.34   |  2/3 ⚠️ |
|   3  | Texas A&M  | 0.917 | 18.68 | 4.85 |   80.23   |   1/3   |
|   4  | Notre Dame | 0.833 | 21.99 | 5.49 |   78.67   |  2/3 ⚠️ |
|   5  | BYU        | 0.917 | 17.86 | 5.19 |   78.59   |  2/3 ⚠️ |
|   6  | Texas Tech | 0.917 | 22.26 | 1.09 |   78.53   |  2/3 ⚠️ |
|   7  | Oregon     | 0.917 | 19.12 | 3.70 |   77.27   |   1/3   |
|   8  | Georgia    | 0.917 | 17.18 | 3.26 |   66.58   |   1/3   |
|   9  | Miami (FL) | 0.833 | 19.25 | 4.25 |   59.93   |   0/3   |
|  10  | Ole Miss   | 0.917 | 15.17 | 3.09 |   55.07   |   1/3   |

#### **Key Insights from IC²:**
- **Texas A&M #3**: Stats-only model recognizes their elite schedule (SOS 4.85) and strong performance
- **Notre Dame #4**: Elite metrics (SRS 21.99, SOS 5.49) despite 2 losses—most polls underrate them
- **0 perfect profiles in 2025**: No team meets all 3 champion criteria
- **Ohio State & Indiana**: Both undefeated but untested (weak schedules may be exposed in playoff)

## Contributing

We welcome contributions! Here's how you can help:

### 🤝 **Reporting Issues**
Found a bug or have a suggestion? [Open an issue](https://github.com/danoff/IC2-Men-s-College-Football-Poll/issues).

### Feature Requests
Suggest new features or improvements:
- Additional statistical features
- Alternative modeling approaches
- Visualization enhancements
- Historical data expansion

### Pull Requests

We like pull requests (PRs)!

### Additional Areas for Contribution
- **Data**: Collect additional seasons or advanced metrics
- **Models**: Experiment with different algorithms
- **Visualization**: Create interactive dashboards
- **Documentation**: Improve methodology explanations
- **Tutorials**
- Testing + CI improvements

## Citation

If you use the IC² Poll in academic work or publications, please cite:

```bibtex
@misc{ic2_poll_2025,
  author = {Danoff, Charles, Battiste, Isaih and Hanes, Christopher},
  title = {IC² Men's College Football Poll: A CFP-Era Statistical Ranking System},
  year = {2025},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/danoff/IC2-Men-s-College-Football-Poll}},
  note = {Logistic regression model trained on CFP-era data (2014-2024). 
        Developed with AI assistance from Claude Sonnet 4.5, ChatGPT 5.1, 
        and DeepSeek V3.2. MPL-2.0 License}
```

## License

This project is licensed under the **Mozilla Public License 2.0**. For full license details, visit: [https://www.mozilla.org/en-US/MPL/2.0/](https://www.mozilla.org/en-US/MPL/2.0/)

## Acknowledgments

**Primary Development**: Charles Danoff, Isaih Battiste, and Chris Hanes  
**Data Sources**: Sports-Reference.com [Sports-Reference CFB](https://www.sports-reference.com/cfb/) for historical CFB data
**Methodological Inspiration**: [Bowl Championship Series](https://en.wikipedia.org/w/index.php?title=Bowl_Championship_Series&oldid=1324107655), [Colley Matrix](https://colleyrankings.com/), [Massey Ratings](https://masseyratings.com/), other advanced metrics  
**Community**: The men's College Football analytics community for ongoing discussions
**AI Tool Assistance**: This project utilized AI programming assistants (ChatGPT, Claude, and others) for code generation, debugging, and methodological discussion. These systems served as advanced tools in the development process—similar to how mathematicians use calculators or writers use thesauruses—extending human capability while the core insights, analytical framework, and final implementation decisions remain human-originated and directed.

## 📋 Requirements

The project requires Python 3.8+ with the following packages:

```
pandas>=1.5.0
numpy>=1.21.0
scikit-learn>=1.0.0
matplotlib>=3.5.0
jupyter>=1.0.0
```
## Contact

- **Charles Danoff** of [Mr. Danoff's Teaching Laboratory](https://teachinglaboratory.com) | 📫 <contact@mr.danoff.org>
- **Isaih Battiste** of Fireball Findings |  Twitter/X [@FireballFinds](https://x.com/FireballFinds)
