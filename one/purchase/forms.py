from django import forms
from .models import Invoice, InvoiceItem, Payment


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['rate', 'balancetype', 'paymenttype', 'balance', 'status', 'supplier']


class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ['weight', 'touch', 'total', 'is_return', 'quantity', 'product', 'invoice']


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['type', 'total', 'description', 'supplier']


