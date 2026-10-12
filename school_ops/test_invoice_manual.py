
from school_ops.reconciliation import reconcile_invoice


invoice = {
    "invoice_id": "INV001",
    "amount": "1000.00",
}

payments = [
    {
        "payment_id": "P101",
        "invoice_id": "INV001",
        "amount": "400.00",
        "status": "POSTED",
    },
    {
        "payment_id": "P102",
        "invoice_id": "INV001",
        "amount": "600.00",
        "status": "PENDING",
    },
]

result = reconcile_invoice(invoice, payments)

print("Invoice:", result["invoice_id"])
print("Total paid:", result["total_paid"])
print("Remaining due:", result["remaining_due"])
print("Status:", result["status"])
