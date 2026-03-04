import pandas as pd
from retail_cleaning import clean_superstore, DataQualityReport

def test_smoke_clean():
    df = pd.DataFrame({'Order ID':['A','A'],'Sales':['$10','10']})
    cleaned, dq = clean_superstore(df)
    assert isinstance(dq, DataQualityReport)
    assert 'Sales' in cleaned.columns
