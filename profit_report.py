# RST-03 — PROFIT REPORT

def profit_by_category(df):
    """
    Returns total sales and profit grouped by category
    """
    return df.groupby('Category')[['Sales', 'Profit']].sum().reset_index()


def profit_by_subcategory(df):
    """
    Returns total sales and profit grouped by sub-category
    """
    return df.groupby('Sub-Category')[['Sales', 'Profit']].sum().reset_index()
import pandas as pd

# Example dataset
data = {
    "Category": ["Furniture", "Furniture", "Technology", "Technology"],
    "Sub-Category": ["Chair", "Table", "Phone", "Laptop"],
    "Sales": [200, 300, 500, 800],
    "Profit": [20, 40, 120, 200]
}

df = pd.DataFrame(data)

print(profit_by_category(df))
print(profit_by_subcategory(df))