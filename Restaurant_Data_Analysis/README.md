# Restaurant Success Analysis — Yelp Open Dataset

A data analyst portfolio project exploring what actually drives restaurant success on Yelp — and whether "more reviews" and "higher ratings" mean the same thing.

**Tech stack:** SQL (SQLite) · Python (pandas, NumPy) · Statistical Testing (SciPy) · NLP Sentiment (VADER) · Time Series (statsmodels) · Geospatial (Folium)

---

## Problem Statement

In a competitive market like the restaurant industry, understanding what drives business success is crucial for stakeholders. This project uses the Yelp Open Dataset to investigate the relationship between user engagement (reviews, tips, check-ins) and business success metrics (review count, average star rating), and to build a more complete picture of what "success" looks like beyond a single number.

## Research Objectives

1. Quantify the correlation between user engagement (reviews, tips, check-ins) and review count / average star rating.
2. Analyze the impact of review sentiment on restaurant ratings, using NLP scoring on actual review text.
3. Explore whether consistent engagement over time is associated with sustained business success.

## Hypotheses & Verdicts

| # | Hypothesis | Verdict |
|---|---|---|
| H1 | Higher user engagement (reviews, tips, check-ins) correlates with higher review counts and ratings | Partially supported — engagement metrics are statistically significant predictors of rating but practically weak (Pearson r ≈ 0.05–0.25) |
| H2 | Positive sentiment in review text is associated with higher star ratings | Strongly supported — VADER sentiment correlates with rating at r ≈ 0.64 |
| H3 | Successful (high-rated) restaurants show consistent, growing engagement over time | Supported — high-rated restaurants sustain higher and more stable review/tip volume across a 5-year window |

## Dataset

The [Yelp Open Dataset](https://www.yelp.com/dataset) covers 150,000+ businesses across 8 North American metro areas, loaded into a local SQLite database (`yelp.db`) with five tables:

| Table | Contents |
|---|---|
| `business` | Name, location, categories, star rating, review count, open status |
| `review` | Star rating, date, full review text, useful/funny/cool votes |
| `tip` | Short user tips with date and business reference |
| `checkin` | Comma-separated string of all check-in timestamps per business |
| `user` | User profiles, including review count and Elite status |

Restaurants are isolated from the broader business table (`categories LIKE '%restaurant%' AND is_open = 1`) before any analysis begins, yielding 35,004 open restaurants. Because review counts are heavily right-skewed (mean of 104 vs. a median of 15, max of 7,568), outliers are removed using the IQR method, leaving 31,537 restaurants with a far more representative average of 56 reviews.

## Methodology

- **Data cleaning:** SQL extraction from SQLite, IQR-based outlier removal on review/check-in/tip counts.
- **Correlation analysis:** Pearson and Spearman correlations between engagement signals (reviews, tips, check-ins) and star rating, with Mann-Whitney U tests comparing high-rated (≥3.5★) vs. low-rated restaurants.
- **Composite success metric:** `success_score = rating × log(review_count + 1)`, normalized to a 0–100 scale, to capture both quality and reach in a single number. Aggregated by metro area and mapped geographically with Folium.
- **Time series analysis:** Monthly review/tip volume (2017–2022) compared between high- and low-rated restaurants, with multiplicative seasonal decomposition (statsmodels) to separate trend, seasonality, and residual.
- **NLP sentiment analysis:** VADER (Valence Aware Dictionary and sEntiment Reasoner) compound scores on a 10,000-review sample, correlated against star ratings.
- **Engagement timing:** Hour-of-day distribution of reviews, tips, and check-ins (check-in timestamps parsed from a comma-separated string field rather than via SQL string manipulation).

## Key Findings

- **Popularity ≠ quality.** The most-reviewed restaurants are large chains (McDonald's, Taco Bell) with mediocre ratings (1.9–2.4★), while the highest-rated spots are mostly small independents with very few reviews.
- **Engagement peaks at 4★, then falls.** Review, check-in, and tip volume rise steadily from 1★ to 4★, then drop at 4.5–5★ — a ceiling effect among small, loyal audiences rather than a linear relationship.
- **Engagement correlates with rating, but weakly.** All three engagement metrics are statistically significant (p < 0.05) but practically weak predictors of rating (Pearson r of 0.08–0.25).
- **Sentiment is a much stronger signal.** Review text sentiment (VADER) correlates with star rating at r ≈ 0.64 — more than twice as strongly as engagement volume — and 85% of sampled reviews score as positive overall.
- **High-rated restaurants sustain engagement.** Across 2017–2022, high-rated restaurants consistently out-pace low-rated ones in monthly review/tip volume, with a clear pandemic-era dip and faster rebound, and a recurring November–March seasonal peak.
- **A small group drives most of the conversation.** Elite users make up just 4.6% of the user base but contribute 56% of total review volume; Useful and Cool votes track success more closely than Funny votes.
- **Engagement concentrates in the evening.** Reviews, tips, and check-ins all peak between 4 PM and 1 AM.
- **Philadelphia leads** on the composite success score among the metro areas studied, combining strong average ratings with high review volume.

## Recommendations

1. **Chase quality, not just volume** — engagement metrics correlate weakly with rating, so focus on experiences that generate genuinely positive reviews rather than simply more of them.
2. **Monitor sentiment, not just stars** — VADER-style sentiment scoring can surface shifts in reputation before aggregate star ratings move.
3. **Target the November–March window** for promotions and launches, the consistently highest-engagement period of the year.
4. **Engage Elite users deliberately** — a small group with outsized influence on public perception.
5. **Benchmark against Philadelphia**, the top-performing metro area on the composite success score.
6. **Staff evening shifts around peak engagement hours** (4 PM–1 AM) to align service quality with the times customers are most likely to review.

**Caveat:** All findings are correlational. Engagement and ratings may reinforce each other over time rather than one causing the other — a causal/longitudinal design would be needed to confirm direction of effect.

## Repository Structure

```
.
├── Restaurant_analysis_improved1.ipynb   # Full analysis notebook (SQL + Python)
├── Restaurant_Success_Analysis.pptx      # Stakeholder-facing summary deck
├── yelp.db                               # SQLite database built from the Yelp Open Dataset (not included — see Setup)
└── README.md
```

## Getting Started

### Prerequisites

```
pandas
numpy
scipy
matplotlib
seaborn
folium
vaderSentiment
statsmodels
jupyter
```

Install with:

```bash
pip install pandas numpy scipy matplotlib seaborn folium vaderSentiment statsmodels jupyter
```

### Setup

1. Download the [Yelp Open Dataset](https://www.yelp.com/dataset) (business, review, tip, checkin, and user JSON files).
2. Load the JSON files into a local SQLite database named `yelp.db` in the project root, with one table per file (`business`, `review`, `tip`, `checkin`, `user`).
3. Launch the notebook:

```bash
jupyter notebook Restaurant_analysis_improved1.ipynb
```

## Project Deliverables

- **`Restaurant_analysis_improved1.ipynb`** — the full technical analysis, including SQL queries, statistical tests, and visualizations.
- **`Restaurant_Success_Analysis.pptx`** — a condensed, stakeholder-facing summary of the methodology and findings.

## Limitations & Future Work

- Findings are correlational; a causal or longitudinal design would be needed to establish direction of effect between engagement and ratings.
- Sentiment analysis uses a 10,000-review sample and a lexicon-based scorer (VADER); a transformer-based model could capture more nuance.
- The composite success score uses a single weighting formula (`rating × log(reviews + 1)`); alternative weightings could be explored and validated against business outcomes (e.g., revenue, longevity).
