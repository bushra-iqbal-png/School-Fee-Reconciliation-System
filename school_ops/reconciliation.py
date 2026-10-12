
def remove_exact_duplicates(payments):
    seen = {}
    unique_payments = []
    duplicates = []

    for payment in payments:
        payment_id = payment["payment_id"]

        if payment_id not in seen:
            seen[payment_id] = payment
            unique_payments.append(payment)

        elif payment == seen[payment_id]:
            duplicates.append(payment_id)

        else:
            raise ValueError(
                f"Conflicting duplicate payment ID: {payment_id}"
            )

    return unique_payments, duplicates


from decimal import Decimal

from school_ops.money import calculate_balance
from school_ops.validation import validate_amount


def reconcile_invoice(invoice, payments):
    invoice_id = invoice["invoice_id"]

    invoice_amount = validate_amount(
        invoice["amount"],
        "Invoice amount"
    )

    unique_payments, duplicates = remove_exact_duplicates(payments)

    total_paid = Decimal("0.00")

    for payment in unique_payments:
        if payment["invoice_id"] != invoice_id:
            continue

        status = payment["status"]

        if status == "POSTED":
            amount = validate_amount(
                payment["amount"],
                "Payment amount"
            )
            total_paid += amount

        elif status == "PENDING":
            continue

        else:
            raise ValueError(
                f"Unsupported payment status: {status}"
            )

    remaining_due, credit = calculate_balance(
        invoice_amount,
        total_paid
    )

    if credit > Decimal("0.00"):
        status = "OVERPAID"
    elif remaining_due == Decimal("0.00"):
        status = "PAID"
    elif total_paid > Decimal("0.00"):
        status = "PARTIALLY PAID"
    else:
        status = "UNPAID"

    return {
        "invoice_id": invoice_id,
        "invoice_amount": invoice_amount,
        "total_paid": total_paid,
        "remaining_due": remaining_due,
        "credit": credit,
        "status": status,
        "duplicates": duplicates,
    }
