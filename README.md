# School Fee Reconciliation System

A Python-based school fee reconciliation tool that processes invoice and payment records from CSV files and generates a clear report showing paid amounts, outstanding balances, and overpayments.

## Features

- Reads invoice and payment records from CSV files.
- Uses Python's `Decimal` for accurate monetary calculations.
- Counts only `POSTED` payments as paid.
- Identifies exact duplicate payments.
- Rejects conflicting duplicate payment IDs.
- Validates invoice and payment amounts.
- Detects payments linked to unknown invoices.
- Calculates outstanding balances without negative values.
- Reports overpayments separately as credits.
- Generates a CSV reconciliation report.
- Includes automated tests using pytest.

## Technologies Used

- Python 3.10+
- CSV
- Decimal
- pytest

## Project Structure

```text
school-operations/
├── school_ops/
│   ├── __init__.py
│   ├── money.py
│   ├── validation.py
│   ├── reconciliation.py
│   └── cli.py
├── sample_data/
│   ├── invoices.csv
│   ├── payments.csv
│   └── reconciliation_report.csv
├── tests/
│   ├── test_money.py
│   ├── test_reconciliation.py
│   ├── test_duplicates.py
│   └── test_validation.py
├── docs/
├── .venv/
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd school-operations
```

Replace `YOUR_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install pytest

```powershell
python -m pip install pytest
```

### 4. Run the reconciliation system

```powershell
python -m school_ops.cli
```

The program reads the CSV files in `sample_data` and creates `reconciliation_report.csv` in the same folder.

### 5. Run automated tests

```powershell
python -m pytest -v
```

## Sample Results

| Invoice Status | Meaning |
|---|---|
| PAID | The invoice has been fully paid. |
| PARTIALLY PAID | Some amount remains outstanding. |
| OVERPAID | The payment exceeds the invoice amount. |
| UNPAID | No posted payment has been received. |

Pending payments are not included in the paid total.

## Data Validation

The system checks monetary values, invoice references, payment statuses, and duplicate payment IDs. Exact duplicate records are counted once, while conflicting records with the same payment ID are rejected.

## Learning Goals

This project demonstrates practical Python skills, including:

- Functions and modules
- CSV file handling
- Decimal-based financial calculations
- Input validation and exception handling
- Data reconciliation
- Automated testing with pytest

## Future Improvements

- Export summary reports with additional filters.
- Add logging and clearer error reports.
- Build a web-based dashboard.
- Add secure user access and database integration.


## Example Output

The reconciliation system produces an invoice-wise report containing the invoice amount, posted payments, outstanding balance, credit amount, and payment status.

Example:

| Invoice ID | Invoice Amount | Total Paid | Outstanding | Credit | Status |
|---|---:|---:|---:|---:|---|
| INV001 | 1000.00 | 1000.00 | 0.00 | 0.00 | PAID |
| INV002 | 1500.00 | 700.00 | 800.00 | 0.00 | PARTIALLY PAID |
| INV003 | 2000.00 | 2500.00 | 0.00 | 500.00 | OVERPAID |
| INV004 | 800.00 | 0.00 | 800.00 | 0.00 | UNPAID |

*These figures illustrate the expected output for the sample records.*

## Running the Tests

Run the automated test suite with:

```powershell
python -m pytest -v
```

## Important Notes

- Only payments with `POSTED` status count toward the paid total.
- `PENDING` payments are excluded from the paid total.
- Exact duplicate payment records are counted once.
- Conflicting records with the same payment ID are rejected.
- Overpayments are reported separately as credits.
- The report is generated as a CSV file that can be opened in spreadsheet software.

## Current Scope

This project is a command-line learning application. It processes CSV files and generates a reconciliation report. It is not yet a complete school management system and does not currently include a web dashboard, database integration, or user authentication.


## Author

**Bushra Iqbal**

Python learner | Web Development Student
