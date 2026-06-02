import pandas as pd

def profile_data(df, name):

    print("\n" + "=" * 60)
    print(f"DATA PROFILE : {name}")
    print("=" * 60)

    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Records:")
    print(df.duplicated().sum())

    print("\nData Types:")
    print(df.dtypes)