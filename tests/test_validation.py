import pytest

from school_ops.validation import validate_payment_batch


def test_valid_batch_is_accepted():
    invoices = [
        {"invoice_id": "INV001", "amount": "1000.00"}
    ]

    payments = [
        {
            "payment_id": "PAY001",
            "invoice_id": "INV001",
            "amount": "500.00",
            "status": "POSTED",
        }
    ]

    assert validate_payment_batch(invoices, payments) is True


def test_unknown_invoice_is_rejected():
    invoices = [
        {"invoice_id": "INV001", "amount": "1000.00"}
    ]

    payments = [
        {
            "payment_id": "PAY001",
            "invoice_id": "INV999",
            "amount": "500.00",
            "status": "POSTED",
        }
    ]

    with pytest.raises(ValueError, match="Unknown invoice ID"):
        validate_payment_batch(invoices, payments)


def test_duplicate_invoice_id_is_rejected():
    invoices = [
        {"invoice_id": "INV001", "amount": "1000.00"},
        {"invoice_id": "INV001", "amount": "800.00"},
    ]

    with pytest.raises(ValueError, match="Duplicate invoice ID"):
        validate_payment_batch(invoices, [])


def test_invalid_payment_amount_is_rejected():
    invoices = [
        {"invoice_id": "INV001", "amount": "1000.00"}
    ]

    payments = [
        {
            "payment_id": "PAY001",
            "invoice_id": "INV001",
            "amount": "-500.00",
            "status": "POSTED",
        }
    ]

    with pytest.raises(ValueError):
        validate_payment_batch(invoices, payments)
