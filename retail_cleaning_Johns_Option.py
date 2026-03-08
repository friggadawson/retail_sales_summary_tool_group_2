import pandas as pd
import matplotlib.pyplot as plt

# RST-01 — DATA LOADING & CLEANING

def clean_dataset(df):
    """
    Cleans the dataset:
    - Converts date columns to datetime
    - Converts Sales and Profit to numeric
    - Drops rows with missing values
    - Adds Profit Margin column
    """

    # Convert dates
    df['Order Date'] = pd.to_datetime(df['Order Date'], format='mixed', dayfirst=True, errors='coerce')
    df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='mixed', dayfirst=True, errors='coerce')

    # Convert numeric columns
    df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
    df['Profit'] = pd.to_numeric(df['Profit'], errors='coerce')

    # Remove invalid rows
    df = df.dropna(subset=['Sales', 'Profit'])

    # Create profit margin
    df['Profit Margin'] = df['Profit'] / df['Sales']

    return df


