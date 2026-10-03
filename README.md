# Loan Covenant Watch

Monitors synthetic borrower metrics against covenant thresholds.

## What it includes

- deterministic sample data
- scoring and ranking logic
- command line report
- unit tests
- continuous validation workflow

## Run

```bash
python3 -m loan_covenant_watch.cli --input data/sample_borrowers.json
```

## Test

```bash
python3 -m unittest discover tests
```
