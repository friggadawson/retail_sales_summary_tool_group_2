# retail_summary.py (fallback)
from typing import Sequence, Union
import pandas as pd, numpy as np
from pathlib import Path
try:
    from retail_cleaning import clean_superstore
except Exception:
    clean_superstore=None
DFLike = Union[str, pd.DataFrame, Path]

def _df(x: DFLike)->pd.DataFrame:
    if isinstance(x,(str,Path)):
        if clean_superstore is None: raise ImportError('need retail_cleaning')
        df,_=clean_superstore(x); return df
    return x.copy()

def sales_by_period(x: DFLike, freq='M')->pd.DataFrame:
    df=_df(x); return df.set_index('Order Date').groupby(pd.Grouper(freq=freq))[['Sales','Quantity']].sum(min_count=1).fillna(0)

def sales_by_dims(x: DFLike, dims: Sequence[str])->pd.DataFrame:
    df=_df(x); return df.groupby(list(dims), dropna=False)[['Sales','Quantity']].sum(min_count=1).sort_values('Sales', ascending=False).reset_index()

def top_n_customers_by_sales(x: DFLike, n:int=10)->pd.DataFrame:
    df=_df(x); return df.groupby(['Customer ID','Customer Name'])[['Sales','Quantity']].sum().sort_values('Sales', ascending=False).head(n).reset_index()

def profit_by_dims(x: DFLike, dims: Sequence[str])->pd.DataFrame:
    df=_df(x); agg=df.groupby(list(dims), dropna=False).agg({'Profit':'sum','Sales':'sum','Quantity':'sum','Discount':'mean'}).reset_index(); agg['Profit Margin']=np.where(agg['Sales']!=0, agg['Profit']/agg['Sales'], np.nan); return agg.sort_values('Profit', ascending=False)

def top_n_products_by_profit(x: DFLike, n:int=10)->pd.DataFrame:
    df=_df(x); return df.groupby(['Product ID','Product Name'])[['Profit','Sales']].sum().sort_values(['Profit','Sales'], ascending=False).head(n).reset_index()

def discount_impact_by_bucket(x: DFLike, bins=(0,0.1,0.2,0.3,1.0))->pd.DataFrame:
    df=_df(x); d=df['Discount'].clip(0,1); bucket=pd.cut(d, bins=bins, include_lowest=True); out=df.assign(DiscountBucket=bucket).groupby('DiscountBucket').agg(Profit=('Profit','sum'), Sales=('Sales','sum')).reset_index(); out['Profit Margin']=np.where(out['Sales']!=0, out['Profit']/out['Sales'], np.nan); return out
