import pytest
from decimal import Decimal

from school_ops.reconciliation import remove_exact_duplicates, reconcile_invoice


def test_exact_duplicate_payment_counted_once():
    invoice = {
        "invoice_id": "INV001",
        "amount": "1000.00",
    }

    payment = {
        "payment_id": "PAY001",
        "invoice_id": "INV001",
        "amount": "400.00",
        "status": "POSTED",
    }

    payments = [payment, payment.copy()]

    result = reconcile_invoice(invoice, payments)

    assert result["total_paid"] == Decimal("400.00")
    assert result["remaining_due"] == Decimal("600.00")
    assert result["duplicates"] == ["PAY001"]


def test_conflicting_duplicate_payment_raises_error():
    payments = [
        {
            "payment_id": "PAY001",
            "invoice_id": "INV001",
            "amount": "400.00",
            "status": "POSTED",
        },
        {
            "payment_id": "PAY001",
            "invoice_id": "INV001",
            "amount": "500.00",
            "status": "POSTED",
        },
    ]

    with pytest.raises(ValueError, match="Conflicting duplicate payment ID"):
        remove_exact_duplicates(payments)
