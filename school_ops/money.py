
from decimal import Decimal


ZERO = Decimal("0.00")


def calculate_balance(invoice_amount, total_paid):
    remaining_due = max(
        invoice_amount - total_paid,
        ZERO
    )

    credit = max(
        total_paid - invoice_amount,
        ZERO
    )

    return remaining_due, credit
