from django import forms
from core.models import PurchaseInvoice, Purchase, Payment

from django.forms.models import inlineformset_factory


class PurchaseInvoiceForm(forms.ModelForm):
    class Meta:
        model = PurchaseInvoice
        fields = ['vendor', 'payment_term', 'status', 'total']


class PurchaseInvoiceItemForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['purchase_invoice', 'item', 'total', 'quantity', 'unit_price', 'note' ]

PurchaseInvoiceItemFormSet=inlineformset_factory(PurchaseInvoice,Purchase,
    fields=('purchase_invoice','item','quantity','unit_price','total',),extra=5,can_delete=True)


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['vendor','purchase_invoice', 'payment_method', 'total', 'description']

