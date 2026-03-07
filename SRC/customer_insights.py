# RST-04 — CUSTOMER INSIGHTS

import pandas as pd


def top_customers_by_sales(df: pd.DataFrame, n: int = 10) -> pd.DataFrame:
    """
    Returns top n customers by total sales
    """
    return (
        df.groupby('Customer Name')['Sales']
          .sum()
          .sort_values(ascending=False)
          .head(n)
          .reset_index()
    )


def top_customers_by_profit(df: pd.DataFrame, n: int = 10) -> pd.DataFrame:
    """
    Returns top n customers by total profit
    """
    return (
        df.groupby('Customer Name')['Profit']
          .sum()
          .sort_values(ascending=False)
          .head(n)
          .reset_index()
    )