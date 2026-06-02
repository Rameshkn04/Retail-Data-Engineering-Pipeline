import pandas as pd
import os
import logging

# =====================================================
# LOGGING CONFIGURATION
# =====================================================

os.makedirs("../Logs", exist_ok=True)

logging.basicConfig(
    filename="../Logs/etl.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="w"
)

logging.info("ETL Pipeline Started")

# =====================================================
# CONFIGURATION
# =====================================================

SOURCE_FILE = "../Data/Bronze/USECASE - Data Engineering.xlsx"

SILVER_PATH = "../Data/Silver/silver_transactions.csv"

os.makedirs("../Data/Silver", exist_ok=True)

# =====================================================
# LOAD DATA
# =====================================================

logging.info("Loading datasets")

product_df = pd.read_excel(
    SOURCE_FILE,
    sheet_name="product_details"
)

retail1_df = pd.read_excel(
    SOURCE_FILE,
    sheet_name="retail_data1"
)

retail2_df = pd.read_excel(
    SOURCE_FILE,
    sheet_name="retail_data2"
)

# =====================================================
# MERGE DATASETS
# =====================================================

transactions_df = pd.concat(
    [retail1_df, retail2_df],
    ignore_index=True
)

print(f"\nInitial Records: {len(transactions_df)}")

# =====================================================
# REMOVE DUPLICATES
# =====================================================

before_count = len(transactions_df)

transactions_df.drop_duplicates(
    subset=["transaction_id"],
    inplace=True
)

after_count = len(transactions_df)

duplicates_removed = before_count - after_count

print(f"Duplicates Removed: {duplicates_removed}")

# =====================================================
# FIX MISSING PRICES
# =====================================================

price_lookup = dict(
    zip(
        product_df["product_id"],
        product_df["price"]
    )
)

transactions_df["price"] = transactions_df.apply(
    lambda row:
    price_lookup[row["product_id"]]
    if pd.isnull(row["price"])
    else row["price"],
    axis=1
)

print("Missing prices fixed")

# =====================================================
# PRODUCT STANDARDIZATION
# =====================================================

product_lookup = dict(
    zip(
        product_df["product_id"],
        product_df["product_name"]
    )
)

transactions_df["product_name"] = (
    transactions_df["product_id"]
    .map(product_lookup)
)

print("Product names standardized")

# =====================================================
# CATEGORY STANDARDIZATION
# =====================================================

category_map = {

    "ELEC": "Electronics",
    "electronics": "Electronics",
    "Electronics": "Electronics",

    "FURN": "Furniture",
    "furniture": "Furniture",
    "Furniture": "Furniture",

    "CLOTH": "Clothing",
    "clothing": "Clothing",
    "Clothing": "Clothing",

    "HOME": "Home Appliances",
    "home appliances": "Home Appliances",
    "Home Appliances": "Home Appliances"
}

transactions_df["category"] = (
    transactions_df["category"]
    .map(category_map)
)

print("Categories standardized")

# =====================================================
# DATE STANDARDIZATION
# =====================================================

transactions_df["transaction_date"] = pd.to_datetime(
    transactions_df["transaction_date"],
    errors="coerce"
)

print("Dates standardized")

# =====================================================
# REMOVE INVALID QUANTITIES
# =====================================================

before_qty = len(transactions_df)

transactions_df = (
    transactions_df[
        transactions_df["quantity"] > 0
    ]
)

after_qty = len(transactions_df)

invalid_qty_removed = (
    before_qty - after_qty
)

print(
    f"Invalid Quantity Records Removed: "
    f"{invalid_qty_removed}"
)

# =====================================================
# EMAIL MASKING
# =====================================================

def mask_email(email):

    try:

        username, domain = email.split("@")

        return (
            username[0]
            + "***@"
            + domain
        )

    except:
        return email


transactions_df["email"] = (
    transactions_df["email"]
    .astype(str)
    .apply(mask_email)
)

print("Emails masked")

# =====================================================
# PHONE MASKING
# =====================================================

def mask_phone(phone):

    phone = str(phone)

    return "******" + phone[-4:]


transactions_df["phone"] = (
    transactions_df["phone"]
    .astype(str)
    .apply(mask_phone)
)

print("Phone numbers masked")

# =====================================================
# REVENUE CALCULATION
# =====================================================

transactions_df["revenue"] = (
    transactions_df["price"]
    * transactions_df["quantity"]
    * (1 - transactions_df["discount"])
)

print("Revenue calculated")

# =====================================================
# DATA QUALITY SUMMARY
# =====================================================

print("\n========== DATA QUALITY SUMMARY ==========")

print(
    f"Final Records: {len(transactions_df)}"
)

print(
    f"Duplicates Removed: {duplicates_removed}"
)

print(
    f"Invalid Quantities Removed: {invalid_qty_removed}"
)

print(
    f"Missing Prices Remaining: "
    f"{transactions_df['price'].isnull().sum()}"
)

print(
    f"Missing Dates Remaining: "
    f"{transactions_df['transaction_date'].isnull().sum()}"
)

print(
    f"Invalid Quantities Remaining: "
    f"{(transactions_df['quantity'] <= 0).sum()}"
)

print(
    f"Total Revenue: "
    f"{transactions_df['revenue'].sum():,.2f}"
)

# =====================================================
# SAVE SILVER LAYER
# =====================================================

transactions_df.to_csv(
    SILVER_PATH,
    index=False
)

print("\nSilver Layer Created Successfully")

print(f"Saved To: {SILVER_PATH}")

print("\nSample Data:")

print(transactions_df.head())


# =====================================================
# CONFIGURATION
# =====================================================

SOURCE_FILE = "../Data/Bronze/USECASE - Data Engineering.xlsx"

SILVER_PATH = "../Data/Silver/silver_transactions.csv"

os.makedirs("../Data/Silver", exist_ok=True)

# =====================================================
# LOAD DATA
# =====================================================


product_df = pd.read_excel(
    SOURCE_FILE,
    sheet_name="product_details"
)

retail1_df = pd.read_excel(
    SOURCE_FILE,
    sheet_name="retail_data1"
)

retail2_df = pd.read_excel(
    SOURCE_FILE,
    sheet_name="retail_data2"
)

# =====================================================
# MERGE DATASETS
# =====================================================

transactions_df = pd.concat(
    [retail1_df, retail2_df],
    ignore_index=True
)

print(f"\nInitial Records: {len(transactions_df)}")

# =====================================================
# REMOVE DUPLICATES
# =====================================================

before_count = len(transactions_df)

transactions_df.drop_duplicates(
    subset=["transaction_id"],
    inplace=True
)

after_count = len(transactions_df)

duplicates_removed = before_count - after_count

print(f"Duplicates Removed: {duplicates_removed}")

# =====================================================
# FIX MISSING PRICES
# =====================================================

price_lookup = dict(
    zip(
        product_df["product_id"],
        product_df["price"]
    )
)

transactions_df["price"] = transactions_df.apply(
    lambda row:
    price_lookup[row["product_id"]]
    if pd.isnull(row["price"])
    else row["price"],
    axis=1
)

print("Missing prices fixed")

# =====================================================
# PRODUCT STANDARDIZATION
# =====================================================

product_lookup = dict(
    zip(
        product_df["product_id"],
        product_df["product_name"]
    )
)

transactions_df["product_name"] = (
    transactions_df["product_id"]
    .map(product_lookup)
)

print("Product names standardized")

# =====================================================
# CATEGORY STANDARDIZATION
# =====================================================

category_map = {

    "ELEC": "Electronics",
    "electronics": "Electronics",
    "Electronics": "Electronics",

    "FURN": "Furniture",
    "furniture": "Furniture",
    "Furniture": "Furniture",

    "CLOTH": "Clothing",
    "clothing": "Clothing",
    "Clothing": "Clothing",

    "HOME": "Home Appliances",
    "home appliances": "Home Appliances",
    "Home Appliances": "Home Appliances"
}

transactions_df["category"] = (
    transactions_df["category"]
    .map(category_map)
)

print("Categories standardized")

# =====================================================
# DATE STANDARDIZATION
# =====================================================

transactions_df["transaction_date"] = pd.to_datetime(
    transactions_df["transaction_date"],
    errors="coerce"
)

print("Dates standardized")

# =====================================================
# REMOVE INVALID QUANTITIES
# =====================================================

before_qty = len(transactions_df)

transactions_df = (
    transactions_df[
        transactions_df["quantity"] > 0
    ]
)

after_qty = len(transactions_df)

invalid_qty_removed = (
    before_qty - after_qty
)

print(
    f"Invalid Quantity Records Removed: "
    f"{invalid_qty_removed}"
)

# =====================================================
# EMAIL MASKING
# =====================================================

def mask_email(email):

    try:

        username, domain = email.split("@")

        return (
            username[0]
            + "***@"
            + domain
        )

    except:
        return email


transactions_df["email"] = (
    transactions_df["email"]
    .astype(str)
    .apply(mask_email)
)

print("Emails masked")

# =====================================================
# PHONE MASKING
# =====================================================

def mask_phone(phone):

    phone = str(phone)

    return "******" + phone[-4:]


transactions_df["phone"] = (
    transactions_df["phone"]
    .astype(str)
    .apply(mask_phone)
)

print("Phone numbers masked")

# =====================================================
# REVENUE CALCULATION
# =====================================================

transactions_df["revenue"] = (
    transactions_df["price"]
    * transactions_df["quantity"]
    * (1 - transactions_df["discount"])
)

print("Revenue calculated")

# =====================================================
# DATA QUALITY SUMMARY
# =====================================================

print("\n========== DATA QUALITY SUMMARY ==========")

print(
    f"Final Records: {len(transactions_df)}"
)

print(
    f"Duplicates Removed: {duplicates_removed}"
)

print(
    f"Invalid Quantities Removed: {invalid_qty_removed}"
)

print(
    f"Missing Prices Remaining: "
    f"{transactions_df['price'].isnull().sum()}"
)

print(
    f"Missing Dates Remaining: "
    f"{transactions_df['transaction_date'].isnull().sum()}"
)

print(
    f"Invalid Quantities Remaining: "
    f"{(transactions_df['quantity'] <= 0).sum()}"
)

print(
    f"Total Revenue: "
    f"{transactions_df['revenue'].sum():,.2f}"
)

# =====================================================
# SAVE SILVER LAYER
# =====================================================

transactions_df.to_csv(
    SILVER_PATH,
    index=False
)

print("\nSilver Layer Created Successfully")

print(f"Saved To: {SILVER_PATH}")

print("\nSample Data:")

print(transactions_df.head())


logging.info(
    f"Final Records: {len(transactions_df)}"
)

logging.info(
    f"Duplicates Removed: {duplicates_removed}"
)

logging.info(
    f"Invalid Quantities Removed: {invalid_qty_removed}"
)

logging.info(
    f"Total Revenue: {transactions_df['revenue'].sum():,.2f}"
)

logging.info(
    "Silver Layer Created Successfully"
)

logging.info(
    "ETL Pipeline Completed Successfully"
)