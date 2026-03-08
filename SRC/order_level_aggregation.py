# RST-06 — ORDER-LEVEL AGGREGATION

import pandas as pd

def aggregate_orders(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregates line items into order-level summaries.

    Parameters
    ----------
    df : pd.DataFrame
        A DataFrame at line-item level with at least:
        ['Order ID', 'Sales', 'Profit', 'Quantity', 'Discount'].

    Returns
    -------
    pd.DataFrame
        One row per 'Order ID' with summed Sales/Profit/Quantity
        and mean Discount.
    """
    return (
        df.groupby('Order ID')
          .agg({
              'Sales': 'sum',
              'Profit': 'sum',
              'Quantity': 'sum',
              'Discount': 'mean'
          })
          .reset_index()
    )