# Retail Sales Summary Tool — Full Pipeline

This package includes a complete, reproducible pipeline:
- Cleaning orchestrator (`SRC/retail_cleaning.py`) returning a cleaned DataFrame + DataQualityReport
- Sales & Profitability summaries (`SRC/retail_summary.py`)
- Tests in `tests/`
- `run_workflow.py` exports cleaned data and summaries to `out/`
- `Makefile` targets: test, demo, dq, summary-demo

## Quick Start
```bash
pip install -r requirements.txt
make test
make summary-demo IN=superstore.csv OUTDIR=out
```
