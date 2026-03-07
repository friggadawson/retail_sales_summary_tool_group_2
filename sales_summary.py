import pandas as pd

# RST-02 — SALES SUMMARY

def sales_by_year(df):
    """
    Returns total sales grouped by year
    """
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    return df.groupby(df['Order Date'].dt.year)['Sales'].sum().reset_index(name='Sales')


def sales_by_region(df):
    """
    Returns total sales grouped by region
    """
    return df.groupby('Region')['Sales'].sum().reset_index()


if __name__ == "__main__":
    data = {
        "Order Date": ["2022-01-10", "2022-03-15", "2023-02-20"],
        "Region": ["East", "West", "East"],
        "Sales": [100, 200, 150]
    }

    df = pd.DataFrame(data)

    print("Sales by Year:")
    print(sales_by_year(df))
    print()

    print("Sales by Region:")
    print(sales_by_region(df))