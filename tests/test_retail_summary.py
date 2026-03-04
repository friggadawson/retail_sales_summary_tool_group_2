import pandas as pd
from retail_summary import sales_by_period, profit_by_dims
from retail_cleaning import clean_superstore

def _mini():
    raw = pd.DataFrame({'Order Date':['2020-01-01','2020-02-01'], 'Sales':[100,200], 'Profit':[10,40], 'Quantity':[1,2], 'Discount':[0,0.1]})
    df,_ = clean_superstore(raw); return df

def test_sales_by_period():
    df=_mini(); out=sales_by_period(df,'M'); assert 'Sales' in out.columns

def test_profit_by_dims():
    df=_mini(); out=profit_by_dims(df,['Order Date']); assert 'Profit Margin' in out.columns
