import pandas as pd
import os

SILVER_FILE = "../Data/Silver/silver_transactions.csv"

GOLD_FOLDER = "../Data/Gold"

import logging

os.makedirs("../Logs", exist_ok=True)

logging.basicConfig(
    filename="../Logs/gold_layer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Gold Layer Creation Started")

os.makedirs(GOLD_FOLDER, exist_ok=True)

print("Loading Silver Layer...")
logging.info("Loading Silver Layer")

df = pd.read_csv(SILVER_FILE)

logging.info(f"Records Loaded: {len(df)}")

# =====================================================
# DIM PRODUCT
# =====================================================

dim_product = (
    df[
        ["product_id",
         "product_name",
         "category"]
    ]
    .drop_duplicates()
)

dim_product.to_csv(
    f"{GOLD_FOLDER}/dim_product.csv",
    index=False
)

# =====================================================
# DIM CITY
# =====================================================

dim_city = (
    df[
        ["city"]
    ]
    .drop_duplicates()
)

dim_city["city_id"] = range(
    1,
    len(dim_city) + 1
)

dim_city.to_csv(
    f"{GOLD_FOLDER}/dim_city.csv",
    index=False
)

# =====================================================
# DIM DATE
# =====================================================

df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

dim_date = pd.DataFrame()

dim_date["date"] = (
    df["transaction_date"]
    .drop_duplicates()
)

dim_date["year"] = (
    dim_date["date"]
    .dt.year
)

dim_date["month"] = (
    dim_date["date"]
    .dt.month
)

dim_date["quarter"] = (
    dim_date["date"]
    .dt.quarter
)

dim_date.to_csv(
    f"{GOLD_FOLDER}/dim_date.csv",
    index=False
)

# =====================================================
# FACT SALES
# =====================================================

fact_sales = df[
    [
        "transaction_id",
        "customer_id",
        "product_id",
        "city",
        "transaction_date",
        "quantity",
        "price",
        "discount",
        "revenue"
    ]
]

fact_sales.to_csv(
    f"{GOLD_FOLDER}/fact_sales.csv",
    index=False
)
logging.info("dim_product.csv created")
logging.info("dim_city.csv created")
logging.info("dim_date.csv created")
logging.info("fact_sales.csv created")
logging.info("revenue_by_city.csv created")
logging.info("revenue_by_category.csv created")
logging.info("monthly_revenue.csv created")
logging.info("top_products.csv created")

# =====================================================
# KPI TABLES
# =====================================================

revenue_by_city = (
    df.groupby("city")
    ["revenue"]
    .sum()
    .reset_index()
)

revenue_by_city.to_csv(
    f"{GOLD_FOLDER}/revenue_by_city.csv",
    index=False
)

revenue_by_category = (
    df.groupby("category")
    ["revenue"]
    .sum()
    .reset_index()
)

revenue_by_category.to_csv(
    f"{GOLD_FOLDER}/revenue_by_category.csv",
    index=False
)

df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

df["year_month"] = (
    df["transaction_date"]
    .dt.strftime("%Y-%m")
)

monthly_revenue = (
    df.groupby("year_month")
    ["revenue"]
    .sum()
    .reset_index()
)
monthly_revenue.to_csv(
    f"{GOLD_FOLDER}/monthly_revenue.csv",
    index=False
)

top_products = (
    df.groupby("product_name")
    ["revenue"]
    .sum()
    .reset_index()
    .sort_values(
        by="revenue",
        ascending=False
    )
)

top_products.to_csv(
    f"{GOLD_FOLDER}/top_products.csv",
    index=False
)

print("\nGold Layer Created Successfully")

print("\nFiles Generated:")

print("""
dim_product.csv
dim_city.csv
dim_date.csv
fact_sales.csv

revenue_by_city.csv
revenue_by_category.csv
monthly_revenue.csv
top_products.csv
""")

logging.info(f"Product Dimension Records: {len(dim_product)}")
logging.info(f"City Dimension Records: {len(dim_city)}")
logging.info(f"Date Dimension Records: {len(dim_date)}")
logging.info(f"Fact Sales Records: {len(fact_sales)}")
logging.info(f"Total Revenue: {df['revenue'].sum():,.2f}")
logging.info("Gold Layer Created Successfully")
logging.info("Gold Layer Pipeline Completed Successfully")