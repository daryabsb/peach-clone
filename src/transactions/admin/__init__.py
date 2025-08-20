from django.contrib import admin
from src.transactions.models import (
    Purchase, Sale, Payment, Receive, Invoice, InvoiceItem, 
    Journal,
)


admin.site.register(Purchase)
admin.site.register(Sale)
admin.site.register(Payment)
admin.site.register(Receive)
admin.site.register(Invoice)
admin.site.register(InvoiceItem)
admin.site.register(Journal)