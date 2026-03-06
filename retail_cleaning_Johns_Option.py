import pandas as pd
import matplotlib.pyplot as plt

# RST-01 — DATA LOADING & CLEANING

def load_dataset(filepath):
    filepath = ("superstore.csv")
    df = pd.read_csv(filepath)
    return df

def clean_dataset(df):

    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Ship Date'] = pd.to_datetime(df['Ship Date'])
    
    df = df.dropna(subset=['Sales', 'Profit'])
    df['Profit Margin'] = df['Profit'] / df['Sales']
    
    return df.head()

