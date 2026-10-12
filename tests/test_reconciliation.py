from decimal import Decimal

from school_ops.reconciliation import reconcile_invoice


def test_fully_paid_invoice():
    invoice = {
        "invoice_id": "INV001",
        "amount": "1000.00",
    }

    payments = [
        {
            "payment_id": "PAY001",
            "invoice_id": "INV001",
            "amount": "1000.00",
            "status": "POSTED",
        }
    ]

    result = reconcile_invoice(invoice, payments)

    assert result["total_paid"] == Decimal("1000.00")
    assert result["remaining_due"] == Decimal("0.00")
    assert result["credit"] == Decimal("0.00")
    assert result["status"] == "PAID"


def test_partial_payment():
    invoice = {
        "invoice_id": "INV002",
        "amount": "1000.00",
    }

    payments = [
        {
            "payment_id": "PAY002",
            "invoice_id": "INV002",
            "amount": "400.00",
            "status": "POSTED",
        }
    ]

    result = reconcile_invoice(invoice, payments)

    assert result["total_paid"] == Decimal("400.00")
    assert result["remaining_due"] == Decimal("600.00")
    assert result["credit"] == Decimal("0.00")
    assert result["status"] == "PARTIALLY PAID"


def test_overpayment():
    invoice = {
        "invoice_id": "INV003",
        "amount": "1000.00",
    }

    payments = [
        {
            "payment_id": "PAY003",
            "invoice_id": "INV003",
            "amount": "1200.00",
            "status": "POSTED",
        }
    ]

    result = reconcile_invoice(invoice, payments)

    assert result["total_paid"] == Decimal("1200.00")
    assert result["remaining_due"] == Decimal("0.00")
    assert result["credit"] == Decimal("200.00")
    assert result["status"] == "OVERPAID"


def test_pending_payment_does_not_count():
    invoice = {
        "invoice_id": "INV004",
        "amount": "1000.00",
    }

    payments = [
        {
            "payment_id": "PAY004",
            "invoice_id": "INV004",
            "amount": "500.00",
            "status": "PENDING",
        }
    ]

    result = reconcile_invoice(invoice, payments)

    assert result["total_paid"] == Decimal("0.00")
    assert result["remaining_due"] == Decimal("1000.00")
    assert result["status"] == "UNPAID"
