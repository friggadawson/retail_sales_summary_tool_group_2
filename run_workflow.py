# run_workflow.py
"""Run the full workflow on superstore.csv and export to /out"""
import argparse, json
from pathlib import Path
from retail_cleaning import clean_superstore
from retail_summary import (
    sales_by_period, sales_by_dims, top_n_customers_by_sales,
    profit_by_dims, top_n_products_by_profit, discount_impact_by_bucket
)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--in', dest='input', required=True)
    ap.add_argument('--outdir', default='out')
    args = ap.parse_args()
    inp = Path(args.input); outdir = Path(args.outdir); outdir.mkdir(parents=True, exist_ok=True)
    df, dq = clean_superstore(inp)
    (outdir/'superstore_cleaned.csv').write_text(df.to_csv(index=False))
    monthly = sales_by_period(df, 'M').reset_index(); monthly.to_csv(outdir/'monthly_sales.csv', index=False)
    by_rc = sales_by_dims(df, ['Region','Category']); by_rc.to_csv(outdir/'sales_by_region_category.csv', index=False)
    top_c = top_n_customers_by_sales(df, 10); top_c.to_csv(outdir/'top_customers_by_sales.csv', index=False)
    pcat = profit_by_dims(df, ['Category']); pcat.to_csv(outdir/'profit_by_category.csv', index=False)
    topp = top_n_products_by_profit(df, 10); topp.to_csv(outdir/'top_products_by_profit.csv', index=False)
    discount_impact_by_bucket(df).to_csv(outdir/'discount_impact.csv', index=False)
    json.dump(dq.to_dict(), open(outdir/'data_quality_report.json','w'), indent=2, default=str)
    print('Wrote outputs to', outdir)

if __name__=='__main__':
    main()
