# 🧩 Capstone Projects

Welcome to **Capstone Projects**, a curated collection of diverse, production-ready projects spanning data analysis, data engineering, NLP, and BI dashboarding. This repository is designed to demonstrate applied skills across the data stack — from raw data pipelines to statistically grounded business insight.

Each project is self-contained in its own folder with clear documentation, dependencies, and reproducible code — ideal for exploring practical implementations or using as a starting point for real-world applications.

---

## 📁 Projects

### 🍽️ [Restaurant Success Analysis](./restaurant_success_analysis) — Yelp Open Dataset
**Domain:** Data Analysis | SQL | Statistical Testing | NLP Sentiment | Time Series

Investigates what actually drives restaurant success on Yelp, testing three explicit hypotheses against engagement (reviews, tips, check-ins), review sentiment, and rating using correlation analysis, significance testing, and seasonal decomposition.
- Pearson/Spearman correlation and Mann-Whitney U testing tied to hypothesis verdicts
- VADER sentiment scoring on review text, correlated against star rating
- Custom composite "success score" benchmarked across metro areas with Folium

### 🏨 [Hotel Booking Cancellations EDA](./hotel_booking_cancellations_eda)
**Domain:** Data Analysis | Python | EDA

An end-to-end exploratory analysis uncovering the drivers behind high cancellation rates at City Hotel and Resort Hotel, pairing seven distinct analyses with strategic, data-backed recommendations.
- 37% overall cancellation rate quantified as a revenue risk
- Price (ADR), seasonality, country, and booking channel isolated as key drivers
- Recommendations mapped directly to specific findings

### 👥 [HR Analytics Dashboard](./hr_analytics_dashboard) — Power BI
**Domain:** Business Intelligence | DAX | Power Query

An interactive two-page Power BI dashboard covering workforce demographics, attrition patterns, and recruitment effectiveness, plus a searchable employee lookup tool.
- Employee Referral identified as the top-performing recruitment channel
- Termination-reason breakdown surfacing career-driven (vs. personal) attrition
- Combines strategic reporting with day-to-day operational lookup

### 💬 [SentimentSync](./sentimentsync)
**Domain:** NLP | Streamlit | Model Benchmarking

A benchmarking tool comparing sentiment analysis techniques — VADER, TextBlob, and Google Gemini — with sentence-level classification, intensity comparisons, and confusion matrices.
- Side-by-side comparison across three distinct sentiment-scoring approaches
- Interactive plots and correlation matrices for model agreement

### 🎬 [MovieLens DBT Project](./movie_data_analysis_using_dbt)
**Domain:** Data Engineering | DBT | Snowflake | AWS S3

A complete ingestion-to-transformation pipeline for the MovieLens 20M dataset, moving data from local storage to S3, into Snowflake, and through modular DBT transformations.
- Automated Snowflake warehouse, schema, and table creation
- Version-controlled, reproducible SQL transformation workflows

### ✈️ [Airline Analytics — Medallion Architecture](./airline_analytics_medallion_architecture)
**Domain:** Data Engineering | Databricks | Lakehouse

A Databricks Lakehouse pipeline implementing the Bronze → Silver → Gold medallion pattern for airline data, with star-schema modeling and orchestration via Lakeflow Pipelines.
- Dynamic data ingestion with Delta Lake
- Star schema design and Slowly Changing Dimension (SCD Type 2) handling

---

## 🔧 Tools & Domains at a Glance

| Project | Domain | Primary Tools |
|---|---|---|
| Restaurant Success Analysis | Data Analysis | SQL, Python, SciPy, VADER, statsmodels, Folium |
| Hotel Booking Cancellations EDA | Data Analysis | Python, pandas, matplotlib, seaborn |
| HR Analytics Dashboard | BI / Dashboarding | Power BI, DAX, Power Query |
| SentimentSync | NLP / Tooling | Streamlit, VADER, TextBlob, Gemini |
| MovieLens DBT Project | Data Engineering | DBT, Snowflake, AWS S3 |
| Airline Analytics (Medallion) | Data Engineering | Databricks, Delta Lake, PySpark, SQL |

---

## 🚀 Getting Started

Clone the repo:

```bash
git clone https://github.com/Shaunjob/capstone_projects.git
cd capstone_projects
```

Each project folder contains its own README with setup instructions, dependencies, and a full write-up of the methodology and findings — start there for anything beyond the summary above.

---

## 👤 Author

Created by Snehashish Chatterjee.
