from school_ops.reconciliation import reconcile_invoice


def test_reconciliation_gives_same_result_every_time():
    invoice = {
        "invoice_id": "INV100",
        "amount": "1000.00",
    }

    payment = {
        "payment_id": "PAY100",
        "invoice_id": "INV100",
        "amount": "300.00",
        "status": "POSTED",
    }

    payments = [payment, payment.copy()]

    first_result = reconcile_invoice(invoice, payments)
    second_result = reconcile_invoice(invoice, payments)

    assert first_result == second_result
    assert str(first_result["total_paid"]) == "300.00"
    assert str(first_result["remaining_due"]) == "700.00"
    assert first_result["duplicates"] == ["PAY100"]


def test_different_payment_ids_are_counted_separately():
    invoice = {
        "invoice_id": "INV200",
        "amount": "1000.00",
    }

    payments = [
        {
            "payment_id": "PAY201",
            "invoice_id": "INV200",
            "amount": "200.00",
            "status": "POSTED",
        },
        {
            "payment_id": "PAY202",
            "invoice_id": "INV200",
            "amount": "200.00",
            "status": "POSTED",
        },
    ]

    result = reconcile_invoice(invoice, payments)

    assert str(result["total_paid"]) == "400.00"
    assert str(result["remaining_due"]) == "600.00"
    assert result["duplicates"] == []
