# RST-07 — VISUALIZATION FUNCTIONS

def plot_sales_trend(df):

    sales_year = sales_by_year(df)
    fig, ax = plt.subplots()
    ax.plot(sales_year['Order Date'], sales_year['Sales'], marker='o')
    ax.set_title("Yearly Sales Trend")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sales")
    return fig


def plot_profit_by_category(df):
    """
    Returns a matplotlib figure for profit by category
    """
    profit_cat = profit_by_category(df)
    fig, ax = plt.subplots()
    ax.bar(profit_cat['Category'], profit_cat['Profit'])
    ax.set_title("Profit by Category")
    ax.set_xlabel("Category")
    ax.set_ylabel("Profit")
    return fig
