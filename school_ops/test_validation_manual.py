
from school_ops.validation import validate_amount


test_values = [
    "1000.00",
    "-500",
    "0",
    "",
    "NaN",
    "Infinity",
    "100.123",
]

for value in test_values:
    try:
        result = validate_amount(value)
        print(f"{value!r}: ACCEPTED -> {result}")
    except ValueError as error:
        print(f"{value!r}: REJECTED -> {error}")
