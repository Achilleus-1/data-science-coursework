# Development and demonstration data

Use Python 3.12: create a virtual environment, then run `python -m pip install
-r requirements.txt`. Run `python tools/check_repository.py` and `python
tools/run_examples.py`. The second command executes all four exercise scripts
headlessly in their own directories. Launch `jupyter notebook` for interactive plots.

The original three CSV datasets were unavailable. The included fdata.csv uses
invented stock prices; Measles.csv and Mumps.csv use deterministic invented counts
for 41 years and 12 months per year, preserving the original expected shape.
They are maintenance demo fixtures, not historical prices, public-health records,
or data suitable for research. Plot labels identify the synthetic example.
These new CSVs may be reused under the maintenance MIT license.

Original hardcoded exercise values and code remain educational examples.
Notebook outputs and execution counts must stay cleared before committing.
