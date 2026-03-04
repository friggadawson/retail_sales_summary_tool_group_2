# retail_cleaning.py (fallback)
from dataclasses import dataclass, asdict
from typing import Dict, Tuple, Union
import pandas as pd, numpy as np, re

@dataclass
class DataQualityReport:
    rows_before: int
    rows_after: int
    duplicate_rows_dropped: int
    numeric_parse_failures: Dict[str, int]
    date_parse_failures: Dict[str, int]
    def to_dict(self):
        return asdict(self)

REQUIRED_COLUMNS = [
    "Row ID","Order ID","Order Date","Ship Date","Ship Mode","Customer ID",
    "Customer Name","Segment","Country","City","State","Postal Code","Region",
    "Product ID","Category","Sub-Category","Product Name","Sales","Quantity",
    "Discount","Profit"
]

NULL_LIKE = {"", " ", "N/A", "NA", "NaN", "NULL", "Null", "none", "None", "null", "$-", "-"}
_num_re = re.compile(r"^[\s]*\(?\$?([+-]?[0-9]*[\.,]?[0-9]+)\)?(?:\s*[A-Za-z$]+)?[\s]*$")

def _num(x):
    if pd.isna(x): return np.nan
    s=str(x).strip()
    if s in NULL_LIKE: return np.nan
    neg=s.startswith('(') and s.endswith(')')
    s2=s.replace(',','')
    m=_num_re.match(s2)
    if m:
        v=float(m.group(1)); return -v if neg and v!=0 else v
    s3=re.sub(r"[^0-9\.-]","", s2)
    if s3 in {"", ".", "-", "-."}: return np.nan
    try: return float(s3)
    except: return np.nan

def _dates(series: pd.Series):
    s = series.astype(str)
    p1 = pd.to_datetime(s, errors='coerce', infer_datetime_format=True)
    needs = p1.isna(); p2 = pd.to_datetime(s[needs], errors='coerce', dayfirst=True)
    out = p1.copy(); out.loc[needs]=p2
    return out.dt.normalize(), int(out.isna().sum())

def clean_superstore(df_or_path: Union[str, pd.DataFrame]) -> Tuple[pd.DataFrame, DataQualityReport]:
    if isinstance(df_or_path, str): df = pd.read_csv(df_or_path)
    else: df = df_or_path.copy()
    rows_before=len(df)
    # normalize nulls & whitespace
    for c in df.columns:
        if df[c].dtype==object or pd.api.types.is_string_dtype(df[c]):
            df[c]=df[c].replace(list(NULL_LIKE), np.nan)
            df[c]=df[c].astype(str).str.replace(r"\s+"," ", regex=True).str.strip().replace({"nan": np.nan})
    # dates
    d_fail={}
    for c in ["Order Date","Ship Date"]:
        if c in df.columns:
            parsed,fail=_dates(df[c]); df[c]=parsed; d_fail[c]=fail
        else: d_fail[c]=0
    # numerics
    n_fail={}
    for c in ["Sales","Quantity","Discount","Profit"]:
        if c in df.columns:
            bna=df[c].isna().sum(); df[c]=df[c].map(_num); n_fail[c]=int(df[c].isna().sum()-bna)
        else: n_fail[c]=0
    # post
    if 'Postal Code' in df.columns:
        df['Postal Code']=df['Postal Code'].astype(str).str.strip().replace({'nan':np.nan})
    for c in REQUIRED_COLUMNS:
        if c not in df.columns: df[c]=np.nan
    df=df.drop_duplicates(); dup=rows_before-len(df)
    return df, DataQualityReport(rows_before,len(df),dup,n_fail,d_fail)
