import pandas as pd


def standardize_categories(df):

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

    df["category"] = df["category"].map(category_map)

    return df


def mask_email(email):

    username, domain = email.split("@")

    return username[0] + "***@" + domain


def mask_phone(phone):

    phone = str(phone)

    return "******" + phone[-4:]