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

This is an open-source men's American/gridiron college football 🏈 poll that provides quantitative rankings based on championship teams from the College Football Playoff era (2014–Present).

## Methodology

More discussion on:
📌 [Reddit](https://www.reddit.com/r/sportsanalytics/comments/1pfbvmj/) ·
📌 [LinkedIn](https://www.linkedin.com/pulse/new-open-source-poll-mens-college-football-surcc) ·
📌 [Twitter/X](https://x.com/FireballFinds/status/1997338915926094094)

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
**AI Tool Assistance**: This project utilized AI programming assistants (ChatGPT, Claude, and others) for code generation, debugging, and methodological discussion. These systems served as advanced tools in the development process—similar to how mathematicians use calculators or writers use thesauruses—extending human capability while the core insights, analytical framework, and final implementation decisions remain human-originated and directed.
- **Data Sources**: Sports-Reference.com [Sports-Reference CFB](https://www.sports-reference.com/cfb/) for historical CFB data
**Methodological Inspiration**: [Bowl Championship Series](https://en.wikipedia.org/w/index.php?title=Bowl_Championship_Series&oldid=1324107655), [Colley Matrix](https://colleyrankings.com/), [Massey Ratings](https://masseyratings.com/), other advanced metrics  
**Community**: The men's College Football analytics community for ongoing discussions

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
