import pandas as pd
import os
import logging

# =====================================================
# LOGGING CONFIGURATION
# =====================================================

os.makedirs("../Logs", exist_ok=True)

logging.basicConfig(
    filename="../Logs/kpi.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("KPI Generation Started")

# =====================================================
# LOAD DATA
# =====================================================

df = pd.read_csv(
    "../Data/Silver/silver_transactions.csv"
)

logging.info(f"Records Loaded: {len(df)}")

# =====================================================
# TOTAL REVENUE
# =====================================================

total_revenue = df["revenue"].sum()

logging.info(
    f"Total Revenue: {total_revenue:,.2f}"
)

# =====================================================
# TOTAL ORDERS
# =====================================================

total_orders = (
    df["transaction_id"]
    .nunique()
)

logging.info(
    f"Total Orders: {total_orders}"
)

# =====================================================
# TOTAL CUSTOMERS
# =====================================================

total_customers = (
    df["customer_id"]
    .nunique()
)

logging.info(
    f"Total Customers: {total_customers}"
)

# =====================================================
# AVERAGE ORDER VALUE
# =====================================================

avg_order_value = (
    total_revenue /
    total_orders
)

logging.info(
    f"Average Order Value: "
    f"{avg_order_value:,.2f}"
)

# =====================================================
# TOP PRODUCT
# =====================================================

top_product = (
    df.groupby("product_name")
    ["revenue"]
    .sum()
    .idxmax()
)

logging.info(
    f"Top Product: {top_product}"
)

# =====================================================
# TOP CITY
# =====================================================

top_city = (
    df.groupby("city")
    ["revenue"]
    .sum()
    .idxmax()
)

logging.info(
    f"Top City: {top_city}"
)

# =====================================================
# KPI DATAFRAME
# =====================================================

kpi_df = pd.DataFrame({

    "Metric": [

        "Total Revenue",
        "Total Orders",
        "Total Customers",
        "Average Order Value",
        "Top Product",
        "Top City"
    ],

    "Value": [

        total_revenue,
        total_orders,
        total_customers,
        avg_order_value,
        top_product,
        top_city
    ]
})

# =====================================================
# SAVE KPI FILE
# =====================================================

kpi_df.to_csv(
    "../Data/Gold/executive_kpis.csv",
    index=False
)

logging.info(
    "executive_kpis.csv created"
)

logging.info(
    "KPI Generation Completed Successfully"
)

# =====================================================
# DISPLAY OUTPUT
# =====================================================

print("\n========== EXECUTIVE KPIs ==========\n")

print(kpi_df)

print(
    "\nKPI file saved to:"
)

print(
    "../Data/Gold/executive_kpis.csv"
)