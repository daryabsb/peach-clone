from django import forms
from core.models import Customer, Item, Invoice, Sale, Receive
from django_select2.forms import Select2Widget,ModelSelect2Widget
# from contact.models import Customer
# from product.models import ProductVariant
from django.forms.models import inlineformset_factory


class InvoiceForm(forms.ModelForm):
    customer=forms.ModelChoiceField(queryset=Customer.objects.all())
    
    class Meta:
        model = Invoice
        fields = [
            'payment_term', 'balance','status','customer'
         
        ]


class InvoiceItemForm(forms.ModelForm):
    item=forms.ModelChoiceField(queryset=Item.objects.all())
    # item=forms.ModelChoiceField(
    #     queryset=Item.objects.all(), 
    # widget = forms.Select(
    #     attrs = {'onchange' : "refresh();"}))


    class Meta:
        model = Sale
        fields = ('invoice', 'item', 'quantity', 'unit_price','total',)

InvoiceItemFormSet=inlineformset_factory(Invoice,Sale,
    fields=('invoice','item','quantity','unit_price','total',),extra=5,can_delete=True)


class ReceiveForm(forms.ModelForm):
    from_account=forms.ModelChoiceField(queryset=Customer.objects.all(),widget=Select2Widget)
    class Meta:
        model = Receive
        fields = ['from_account', 'invoice', 'payment_method', 'amount', 'description']
