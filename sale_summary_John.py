# RST-02 — SALES SUMMARY

def sales_by_year(df):
    """
    Returns total sales grouped by year
    """
    # Introduce an error: incorrect column name
    return df.groupby('Order Year')['Sales'].sum().reset_index()  # 'Order Year' does not exist


def sales_by_region(df):
    """
    Returns total sales grouped by region
    """
    return df.groupby('Region')['Sales'].sum().reset_index()