
from school_ops.validation import validate_payment_batch


invoices = [
    {
        "invoice_id": "INV001",
        "amount": "1000.00",
    }
]

payments = [
    {
        "payment_id": "P101",
        "invoice_id": "INV001",
        "amount": "400.00",
        "status": "POSTED",
    }
]

try:
    validate_payment_batch(invoices, payments)
    print("Batch validation successful!")
except ValueError as error:
    print("Batch rejected:", error)
