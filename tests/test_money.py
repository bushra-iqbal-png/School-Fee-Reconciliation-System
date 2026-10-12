
from decimal import Decimal

from school_ops.money import calculate_balance


def test_fully_paid():
    due, credit = calculate_balance(
        Decimal("1000.00"),
        Decimal("1000.00"),
    )

    assert due == Decimal("0.00")
    assert credit == Decimal("0.00")


def test_partial_payment():
    due, credit = calculate_balance(
        Decimal("1000.00"),
        Decimal("400.00"),
    )

    assert due == Decimal("600.00")
    assert credit == Decimal("0.00")


def test_overpayment():
    due, credit = calculate_balance(
        Decimal("1000.00"),
        Decimal("1100.00"),
    )

    assert due == Decimal("0.00")
    assert credit == Decimal("100.00")
