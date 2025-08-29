# airline_analytics_medallion_architecture

**airline_analytics_medallion_architecture** is a Databricks project that demonstrates how to build an **Airline Analytics Data Lakehouse** using the **Medallion Architecture**.  

The project showcases real-world data engineering practices such as dynamic ingestion, star schema modeling, and handling slowly changing dimensions — all orchestrated within Databricks.

---

## Features

- Automated **dynamic data ingestion** from raw to bronze  
- Implementation of the **Medallion Architecture** (Bronze → Silver → Gold)  
- Usage of **Lakeflow Pipelines** for ETL orchestration  
- **Star Schema** design for analytical queries  
- Support for **Slowly Changing Dimensions (SCD Type 2)**  
- Demonstrates **Databricks-native best practices** for scalable pipelines  

---

## Tech Stack

- **Databricks** (Lakehouse Platform)  
- **Lakeflow Pipelines** for orchestration  
- **Delta Lake** for ACID-compliant storage  
- **PySpark** for ETL logic  
- **SQL** for schema design and transformations  

---

## Project Structure
### airline_analytics_medallion_architecture.dbc
- setup/ # To setup initial project-
- raw/ # Landing zone for raw CSV files
- bronze/ # Ingested and minimally transformed data
- silver/ # Cleansed, conformed, and SCD-applied data
- gold/ # Star schema and analytics-ready data
- notebooks/ # Databricks notebooks for ingestion & transformations
- DLT ── dltPipeline.py/ # Lakeflow Scripts