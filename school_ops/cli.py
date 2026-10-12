import csv
from pathlib import Path

from school_ops.reconciliation import reconcile_invoice
from school_ops.validation import validate_payment_batch


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "sample_data"


def read_csv(filename):
    file_path = DATA_DIR / filename

    with file_path.open("r", encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


def main():
    invoices = read_csv("invoices.csv")
    payments = read_csv("payments.csv")

    # Validate all invoices and payments before processing.
    validate_payment_batch(invoices, payments)

    report_rows = []

    print("\nSCHOOL FEE RECONCILIATION REPORT")
    print("=" * 70)

    for invoice in invoices:
        related_payments = [
            payment
            for payment in payments
            if payment["invoice_id"] == invoice["invoice_id"]
        ]

        result = reconcile_invoice(invoice, related_payments)

        report_row = {
            "invoice_id": result["invoice_id"],
            "student_name": invoice["student_name"],
            "invoice_amount": f"{result['invoice_amount']:.2f}",
            "total_paid": f"{result['total_paid']:.2f}",
            "outstanding": f"{result['remaining_due']:.2f}",
            "credit": f"{result['credit']:.2f}",
            "status": result["status"],
        }

        report_rows.append(report_row)

        print(f"\nInvoice ID: {report_row['invoice_id']}")
        print(f"Student: {report_row['student_name']}")
        print(f"Invoice Amount: {report_row['invoice_amount']}")
        print(f"Total Paid: {report_row['total_paid']}")
        print(f"Outstanding: {report_row['outstanding']}")
        print(f"Credit: {report_row['credit']}")
        print(f"Status: {report_row['status']}")

        if result["duplicates"]:
            print(f"Duplicate payments: {result['duplicates']}")

    # Save the report as a CSV file.
    report_path = DATA_DIR / "reconciliation_report.csv"

    fieldnames = [
        "invoice_id",
        "student_name",
        "invoice_amount",
        "total_paid",
        "outstanding",
        "credit",
        "status",
    ]

    with report_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(report_rows)

    print("\n" + "=" * 70)
    print("Reconciliation completed successfully!")
    print(f"Report saved to: {report_path}")


if __name__ == "__main__":
    main()