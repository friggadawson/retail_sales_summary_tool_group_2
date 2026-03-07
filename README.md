![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-green)
![Agile](https://img.shields.io/badge/Methodology-Agile-blueviolet)

# retail_sales_summary_tool_group_2
Group 2's Agile sprint project: Building a modular Python Retail Sales Summary Tool that loads, cleans, and analyzes the superstore.csv dataset to generate insights like sales/profit by category/region, top customers/products, and margins—ready for dashboard integration. One-week sprint tracked via Taiga and GitHub.

# Detailed Description

It is a Python-based analytics tool that processes the Superstore retail dataset: superstore.csv, to generate meaningful business insights. The tool reads and cleans the dataset, summarizes sales and profit performance, identifies customer and product insights, aggregates orders, and provides simple visualization functions.

The project was designed with **modular and reusable Python functions** so the results can later be integrated into visualization tools such as dashboards.

## Dataset

The dataset used in this project is **Superstore Sales Data**.

Important characteristic of the dataset:

- The data is stored at the **line-item level**
- Each row represents **one product within an order**
- A single **Order ID may appear across multiple rows**
- Sales, Quantity, Discount, and Profit apply only to that individual product line

## Following are the features (functions)

### Data Loading and Cleaning
Loads the dataset and prepares it for analysis.

Functions:
- `load_dataset()`
- `clean_dataset()`

Cleaning steps include:
- Converting date columns to datetime format
- Removing rows with missing Sales or Profit
- Creating a Profit Margin column

### Sales Analysis

Generates sales summaries to analyze revenue performance.

Functions:
- `sales_by_year()`
- `sales_by_region()`


### Profit Analysis

Provides profitability insights by product category.

Functions:
- `profit_by_category()`
- `profit_by_subcategory()`



### Customer Insights

Identifies top customers based on revenue and profit.

Functions:
- `top_customers_by_sales()`
- `top_customers_by_profit()`



### Product Performance

Evaluates the performance of products based on sales and profitability.

Functions:
- `top_products_by_sales()`
- `least_profitable_products()`



### Order-Level Aggregation

Aggregates line-item records into order-level summaries.

Function:
- `aggregate_orders()`



### Visualization

Provides reusable visualizations using Matplotlib.

Functions:
- `plot_sales_trend()`
- `plot_profit_by_category()`

These functions return **Matplotlib figure objects** that can be used in other applications such as dashboards.

## Installation

Clone the repository: https://github.com/friggadawson/retail_sales_summary_tool_group_2.git

Navigate into the project directory:
Install the required dependencies:

## Example Usage

```python
import retail_sales_tool_clean as rst

df = rst.load_dataset("superstore.csv")
df = rst.clean_dataset(df)

print(rst.sales_by_region(df))

top_customers = rst.top_customers_by_sales(df)
print(top_customers)

fig = rst.plot_sales_trend(df)
fig.show()

## Technologies Used:

Python
Pandas
Matplotlib
Git & GitHub
Contributors

Developed by the project Group 2 members as part of our Agile software development assignment.

