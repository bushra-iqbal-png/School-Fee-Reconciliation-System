
from decimal import Decimal
from school_ops.money import calculate_balance


invoice = Decimal("1000.00")
paid = Decimal("1100.00")

remaining_due, credit = calculate_balance(invoice, paid)

print("Remaining due:", remaining_due)
print("Credit:", credit)
