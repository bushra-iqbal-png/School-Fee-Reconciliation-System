
from decimal import Decimal, InvalidOperation


def validate_amount(value, field_name="Amount"):
    if value is None or not str(value).strip():
        raise ValueError(f"{field_name} cannot be blank.")

    try:
        amount = Decimal(str(value).strip())
    except (InvalidOperation, ValueError):
        raise ValueError(f"{field_name} must be a valid number.")

    if not amount.is_finite():
        raise ValueError(f"{field_name} must be finite.")

    if amount <= Decimal("0"):
        raise ValueError(f"{field_name} must be greater than zero.")

    if amount.as_tuple().exponent < -2:
        raise ValueError(
            f"{field_name} cannot have more than 2 decimal places."
        )

    return amount



def validate_payment_batch(invoices, payments):
    invoice_ids = set()

    for invoice in invoices:
        invoice_id = invoice.get("invoice_id")

        if not invoice_id:
            raise ValueError("Invoice ID cannot be blank.")

        if invoice_id in invoice_ids:
            raise ValueError(
                f"Duplicate invoice ID: {invoice_id}"
            )

        validate_amount(
            invoice.get("amount"),
            f"Invoice {invoice_id} amount"
        )

        invoice_ids.add(invoice_id)

    seen_payments = {}

    for payment in payments:
        payment_id = payment.get("payment_id")
        invoice_id = payment.get("invoice_id")

        if not payment_id:
            raise ValueError("Payment ID cannot be blank.")

        if not invoice_id:
            raise ValueError(
                f"Invoice ID missing for payment {payment_id}."
            )

        if invoice_id not in invoice_ids:
            raise ValueError(
                f"Unknown invoice ID {invoice_id} "
                f"for payment {payment_id}."
            )

        if payment_id in seen_payments:
            if payment != seen_payments[payment_id]:
                raise ValueError(
                    f"Conflicting duplicate payment ID: "
                    f"{payment_id}"
                )
        else:
            seen_payments[payment_id] = payment

        status = payment.get("status")

        if status not in ("POSTED", "PENDING"):
            raise ValueError(
                f"Unsupported payment status for {payment_id}."
            )

        validate_amount(
            payment.get("amount"),
            f"Payment {payment_id} amount"
        )

    return True
