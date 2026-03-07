.PHONY: test demo dq summary-demo

test:
	pytest -q

demo:
	python -m retail_cleaning superstore.csv --out out/superstore_cleaned.csv || true

dq:
	python -c "import webbrowser; webbrowser.open('DQ_report_demo.ipynb')"

summary-demo:
	python run_workflow.py --in $(IN) --outdir $(OUTDIR)
