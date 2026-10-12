
from school_ops.reconciliation import remove_exact_duplicates


payments = [
    {
        "payment_id": "P101",
        "invoice_id": "INV001",
        "amount": "400.00",
        "status": "POSTED",
    },
    {
        "payment_id": "P101",
        "invoice_id": "INV001",
        "amount": "400.00",
        "status": "POSTED",
    },
]

unique_payments, duplicates = remove_exact_duplicates(payments)

print("Unique payments:", len(unique_payments))
print("Duplicate IDs:", duplicates)
