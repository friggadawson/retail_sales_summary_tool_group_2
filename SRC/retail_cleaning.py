import pandas as pd

def clean_superstore(df):

    report = {}

    # Remove duplicate rows
    rows_before = len(df)
    df = df.drop_duplicates()
    report["duplicates_removed"] = rows_before - len(df)

    # Handle missing values
    report["missing_values_before"] = df.isnull().sum().sum()
    df = df.dropna()
    report["missing_values_after"] = df.isnull().sum().sum()

    return df, report