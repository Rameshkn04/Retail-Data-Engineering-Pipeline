# 🏪 Retail Data Engineering Pipeline

> End-to-End Retail Data Engineering Pipeline using Python, Medallion Architecture, ETL Processing, KPI Engine, Logging Framework, and Power BI Dashboards.

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square\&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-blue?style=flat-square\&logo=pandas)
![Power BI](https://img.shields.io/badge/PowerBI-Dashboard-yellow?style=flat-square)
![Architecture](https://img.shields.io/badge/Architecture-Medallion-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---

# 📖 Project Overview

This project demonstrates the implementation of a complete Retail Data Engineering Pipeline following the Medallion Architecture (Bronze → Silver → Gold).

The pipeline ingests raw retail transaction data from Excel files, performs data cleansing and transformation using Python and Pandas, generates analytical datasets and KPIs, and delivers business insights through interactive Power BI dashboards.

The project simulates a real-world Data Engineering workflow used by modern analytics teams.

---

# 🎯 Business Problem

Retail organizations generate large amounts of transactional data every day.

Common challenges include:

* Duplicate records
* Missing values
* Invalid quantities
* Inconsistent categories
* Multiple date formats
* Sensitive customer information

Without proper processing, business reporting becomes unreliable.

This project solves these challenges by creating a structured ETL pipeline that converts raw retail data into analytics-ready datasets.

---

# 🏗️ Solution Architecture

## Current Architecture

> Insert Architecture Image

```text
Architecture/Current_Architecture.png
```

### Architecture Flow

Raw Excel Files
↓
Bronze Layer
↓
Python ETL Pipeline
↓
Silver Layer
↓
Gold Layer
↓
KPI Engine
↓
Power BI Dashboards

---

# 🥉 Bronze Layer

The Bronze Layer stores raw source files without modifications.

### Source Datasets

| Dataset         | Rows |
| --------------- | ---- |
| product_details | 10   |
| retail_data1    | 4243 |
| retail_data2    | 4251 |

Total Raw Records: 8494

---

# 🥈 Silver Layer

The Silver Layer contains cleaned and standardized datasets.

### ETL Operations

* Merge datasets
* Remove duplicates
* Handle missing prices
* Standardize product names
* Standardize categories
* Standardize dates
* Remove invalid quantities
* Mask email addresses
* Mask phone numbers
* Calculate revenue

### Silver Layer Process Flow

> Insert Process Flow Diagram

```text
Architecture/Silver_Layer_Process_Flow.png
```

### Data Quality Results

| Metric                     | Value |
| -------------------------- | ----- |
| Raw Records                | 8494  |
| Duplicate Records Removed  | 494   |
| Invalid Quantities Removed | 86    |
| Final Records              | 7914  |

---

# 🥇 Gold Layer

Business-ready datasets generated from the Silver Layer.

## Fact Table

* fact_sales.csv

## Dimension Tables

* dim_product.csv
* dim_city.csv
* dim_date.csv

## Aggregated Tables

* revenue_by_city.csv
* revenue_by_category.csv
* monthly_revenue.csv
* top_products.csv

---

# 📊 KPI Engine

Generated Executive KPIs:

| KPI                 | Value         |
| ------------------- | ------------- |
| Total Revenue       | ₹1.16 Billion |
| Total Orders        | 7,914         |
| Total Customers     | 1,960         |
| Average Order Value | ₹147,080      |
| Top Product         | Laptop        |
| Top City            | Chennai       |

Output:

```text
Data/Gold/executive_kpis.csv
```

---

# 📈 Power BI Dashboards

The project contains five interactive dashboards.

## Executive Summary Dashboard

Features:

* Total Revenue
* Total Orders
* Total Customers
* Average Order Value
* Revenue by Category
* Revenue by City

Screenshot:

```text
Screenshots/Executive_Summary.png
```

---

## Revenue Trends Dashboard

Features:

* Monthly Revenue Trend
* Revenue by City
* Revenue Summary Table

Screenshot:

```text
Screenshots/Revenue_Trends.png
```

---

## Product Performance Dashboard

Features:

* Top Products by Revenue
* Product Revenue Distribution
* Maximum Revenue KPI

Screenshot:

```text
Screenshots/Product_Performance.png
```

---

## Category Analysis Dashboard

Features:

* Category Performance Comparison
* Revenue Contribution by Category
* Revenue Distribution by Category

Screenshot:

```text
Screenshots/Category_Analysis.png
```

---

## Regional Analysis Dashboard

Features:

* Top Performing City
* Revenue by City
* Revenue Share by City

Screenshot:

```text
Screenshots/Regional_Analysis.png
```

---

# 📂 Project Structure

Retail-Data-Engineering/

├── Architecture/

├── Code/

├── Data/

│   ├── Bronze/

│   ├── Silver/

│   └── Gold/

├── Documentation/

├── Logs/

├── PowerBI/

├── Screenshots/

├── requirements.txt

└── README.md

---

# 📝 Logging & Monitoring

The project includes logging for operational monitoring.

Generated Logs:

* etl.log
* gold_layer.log
* kpi.log

Logged Information:

* Pipeline execution status
* Record counts
* Data quality metrics
* KPI calculations
* Success/failure tracking

---

# ⚙️ Technologies Used

| Technology | Purpose               |
| ---------- | --------------------- |
| Python     | ETL Development       |
| Pandas     | Data Processing       |
| NumPy      | Data Manipulation     |
| Excel      | Source Data           |
| Power BI   | Dashboard Development |
| Draw.io    | Architecture Design   |
| GitHub     | Version Control       |
| Logging    | Pipeline Monitoring   |

---

# 🚀 How to Run

### Clone Repository

```bash
git clone <repository-url>
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run ETL Pipeline

```bash
python Code/retail_etl.py
```

### Generate Gold Layer

```bash
python Code/gold_layer.py
```

### Generate KPIs

```bash
python Code/executive_kpis.py
```

### Open Power BI Dashboard

```text
PowerBI/Retail_Data_Engineering_Dashboard.pbix
```

---

# ☁️ Future Azure Architecture

Planned Enterprise Architecture:

* Azure Data Lake Gen2
* Azure Data Factory
* Azure Databricks
* Azure SQL Database
* Power BI Service

> Insert Azure Architecture Diagram

```text
Architecture/Azure_Future_Architecture.png
```

---

# 🎯 Key Achievements

✔ Implemented Medallion Architecture

✔ Built End-to-End ETL Pipeline

✔ Performed Data Cleaning & Transformation

✔ Generated Business KPIs

✔ Developed Interactive Power BI Dashboards

✔ Implemented Logging Framework

✔ Designed Future Azure Data Platform Architecture

---

# 👨‍💻 Author

Ramesh K N

Data Engineering | Python | SQL | Power BI | ETL | Analytics

---

# 📄 License

This project is developed for educational, portfolio, and learning purposes.
