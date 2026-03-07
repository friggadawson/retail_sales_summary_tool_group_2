import pandas as pd
from retail_cleaning import clean_superstore


def product_performance():

    # 1. Load dataset
    df = pd.read_csv("data/raw/superstore.csv", encoding="latin1")

    # 2. Clean dataset
    df, report = clean_superstore(df)

    # 3. Top selling products
    top_selling = (
        df.groupby("Product Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    # 4. Least profitable products
    least_profitable = (
        df.groupby("Product Name")["Profit"]
        .sum()
        .sort_values()
        .head(10)
    )

    # 5. Save results to Reports folder
    top_selling.to_csv("Reports/top_selling_products.csv")
    least_profitable.to_csv("Reports/least_profitable_products.csv")

    return top_selling, least_profitable, report


if __name__ == "__main__":

    top_selling, least_profitable, report = product_performance()

    print("\nTop Selling Products:\n")
    print(top_selling)

    print("\nLeast Profitable Products:\n")
    print(least_profitable)

    print("\nCleaning Report:\n")
    print(report)