# MovieLens DBT Project



[![DBT](https://img.shields.io/badge/DBT-v1.9.0-blue)](https://www.getdbt.com/)  

[![Snowflake](https://img.shields.io/badge/Snowflake-Data%20Warehouse-blue)](https://www.snowflake.com/)  

[![AWS S3](https://img.shields.io/badge/AWS%20S3-Storage-orange)](https://aws.amazon.com/s3/)  



A complete **DBT + Snowflake + AWS S3** project to process and transform the **MovieLens 20M dataset**.



---



## Table of Contents

- [1. Download Dataset](#1-download-the-dataset)

- [2. Create AWS S3 Bucket](#2-create-an-aws-s3-bucket)

- [3. Install AWS CLI](#3-install-aws-cli)

- [4. Configure AWS CLI](#4-on-terminal-use)

- [5. Enter AWS Credentials](#5-enter-your-credentials-and-regions)

- [6. Upload Dataset to S3](#6-upload-the-dataset-to-aws-from-local-directory-to-s3)

- [7. Snowflake Setup](#7-snowflake-database-and-schema-declaration)

- [8. Load Data from S3 to Snowflake](#8-copy-the-data-from-s3-to-snowflake)

- [9. Setup DBT Project](#9-setup-dbt-project-in-your-ide-vscode-example)

- [10. Explore DBT Files](#10-use-the-dbt-files-to-go-through-each-and-every-folder)



---



## **1. Download the dataset**

[MovieLens 20M Dataset](https://grouplens.org/datasets/movielens/20m/)



---



## **2. Create an AWS S3 Bucket**

**Note:** Bucket name should be universally unique.



## **3. Install AWS CLI**



## **4. On terminal use**

aws configure



## **5. Enter your credentials and regions**



## **6. Upload the Dataset to AWS from local directory to S3**

aws s3 cp . s3://{your_bucket_name} --recursive --exclude "*" --include "*.csv"



## **7. Snowflake Database and Schema Declaration**

File is present in the project [snowflake_schema_declaration.sql]



## **8. Copy the data from S3 to Snowflake**

File is present in the project [s3_to_snowflake.sql]



## **9. Setup DBT Project in Your IDE (VSCode Example)**

### **1. Create & activate virtual environment**

-- Windows

virtualenv venv

&nbsp;.venvScriptsActivate.ps1



-- MacOS

virtualenv venv

source venv/bin/activate



### **2. Install dbt & respective modules**

pip install dbt dbt-snowflake==1.9.0



### **3.Make a new Directory in your system to store the credentials**

-- Windows

mkdir %userprofile%.dbt



-- MacOS

mkdir ~/.dbt





## **4. Initialize the dbt project and connect to Snowflake**

dbt init



## **10. Study the project files and understand the use case**

