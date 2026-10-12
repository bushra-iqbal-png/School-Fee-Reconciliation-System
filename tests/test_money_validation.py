import pytest

from school_ops.validation import validate_amount


@pytest.mark.parametrize(
    "value",
    [
        "",
        "   ",
        "-100",
        "0",
        "NaN",
        "Infinity",
        "-Infinity",
        "abc",
        "12.345",
    ],
)
def test_invalid_amounts_are_rejected(value):
    with pytest.raises(ValueError):
        validate_amount(value)


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("100", "100"),
        ("100.50", "100.50"),
        ("0.01", "0.01"),
    ],
)
def test_valid_amounts_are_accepted(value, expected):
    result = validate_amount(value)

    assert str(result) == expected
