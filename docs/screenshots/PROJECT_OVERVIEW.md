# School Fee Reconciliation System — Project Overview

## 1. Introduction

The School Fee Reconciliation System is a Python command-line application designed to compare school fee invoices with payment records.

It processes CSV files, validates financial data, calculates outstanding balances, identifies overpayments, and generates a reconciliation report.

## 2. Problem Statement

Schools need to compare the fees charged to students with the payments received. Manually checking these records can take time and may lead to calculation errors or duplicate payment records.

This project demonstrates how Python can automate important parts of this process and produce a consistent report.

## 3. Project Objectives

- Reconcile invoices with their related payments.
- Calculate total paid amounts and outstanding balances.
- Exclude pending payments from the paid total.
- Detect duplicate payment records.
- Identify conflicting payment IDs.
- Track overpayments separately as credit.
- Export reconciliation results to a CSV file.
- Verify application logic through automated tests.

## 4. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Decimal | Accurate financial calculations |
| CSV | Reading input data and exporting reports |
| Pytest | Automated testing |
| Git and GitHub | Version control and project hosting |

## 5. How the System Works

1. The application reads invoice and payment records from CSV files.
2. It validates the financial amounts and payment references.
3. It checks for duplicate or conflicting payment IDs.
4. It counts eligible posted payments and excludes pending payments.
5. It calculates the outstanding balance and any credit.
6. It assigns a reconciliation status to each invoice.
7. It displays the results in the terminal.
8. It exports the results to a CSV report.

## 6. Business Rules

- Invoice and payment amounts must be greater than zero.
- Monetary values may contain no more than two decimal places.
- Only `POSTED` payments count towards the paid total.
- `PENDING` payments do not reduce the outstanding balance.
- Identical duplicate payment records should be counted only once.
- Conflicting records with the same payment ID must be rejected.
- Payments must reference existing invoices.
- Outstanding balances cannot be negative.
- Overpayments are reported separately as credit.

## 7. Reconciliation Statuses

| Status | Meaning |
|---|---|
| `UNPAID` | No posted payment has been received. |
| `PARTIALLY PAID` | Some of the invoice amount has been paid. |
| `PAID` | The invoice amount has been paid exactly. |
| `OVERPAID` | Payments exceed the invoice amount, creating a credit. |

## 8. Testing

The project includes automated tests for financial calculations, invoice reconciliation, duplicate detection, input validation, and repeatability.

Run the tests using:

```bash
python -m pytest -v
```

The documented test coverage should match the tests actually present in the repository.

## 9. Current Scope and Limitations

This is a command-line application that uses CSV files. It does not currently provide a web interface, database integration, online fee collection, or user authentication.

## 10. Future Enhancements

- Database integration for persistent records.
- A web-based dashboard for school administrators.
- User authentication and role-based access.
- Additional financial summaries and downloadable reports.
- Integration with an authorized payment provider.

## 11. Learning Outcomes

This project demonstrates practical experience with Python functions, CSV processing, financial calculations, input validation, exception handling, automated testing, and version control.