from django.forms import ModelForm
from django import forms

from core.models import (
    Company,
    Owner,
    AccountMain,
    AccountSub,
    Item,
    Purchase,
    Customer,
    Vendor,
    Sale,
    Payment,
    Receive)

class PurchaseForm(forms.ModelForm):
    department = forms.ModelChoiceField(queryset=Company.objects.all(), empty_label="Select your department")
    vendor = forms.ModelChoiceField(queryset=Vendor.objects.all(), empty_label="Select a vendor")
    item = forms.ModelChoiceField(queryset=Item.objects.all(), empty_label="Select an item")

    class Meta:
        model = Purchase
        fields = (
            'department','vendor','description',
            'item','quantity','unit_price','note',
            )

    def __init__(self, *args,**kwargs):
        super(PurchaseForm, self).__init__(*args,**kwargs)
        self.fields['department'].widget.attrs.update({'class': 'form-control'})
        self.fields['vendor'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({
            'class': 'form-control', 
            'rows':5, 
            'placeholder':'Please describe the item!'
            })
        self.fields['item'].widget.attrs.update({'class': 'form-control'})
        self.fields['quantity'].widget.attrs.update({'class': 'form-control'})
        self.fields['unit_price'].widget.attrs.update({'class': 'form-control'})
        self.fields['note'].widget.attrs.update({'class': 'form-control'})

class SaleForm(forms.ModelForm):
    
    department = forms.ModelChoiceField(queryset=Company.objects.all(), empty_label="Select your department")
    customer = forms.ModelChoiceField(queryset=Customer.objects.all(), empty_label="Select a customer")
    item = forms.ModelChoiceField(queryset=Item.objects.all(), empty_label="Select an item")

    class Meta:
        model = Sale
        fields = (
            'department','customer','description',
            'item','quantity','unit_price','note',
            )

    def __init__(self, *args,**kwargs):
        super(SaleForm, self).__init__(*args,**kwargs)
        self.fields['department'].widget.attrs.update({'class': 'form-control'})
        self.fields['customer'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({
            'class': 'form-control', 
            'rows':5, 
            'placeholder':'Please describe the item!'
            })
        self.fields['item'].widget.attrs.update({'class': 'form-control'})
        self.fields['quantity'].widget.attrs.update({'class': 'form-control'})
        self.fields['unit_price'].widget.attrs.update({'class': 'form-control'})
        self.fields['note'].widget.attrs.update({'class': 'form-control'})

class PaymentForm(forms.ModelForm):
    
    from_account = forms.ModelChoiceField(queryset=Company.objects.all(), empty_label="Select your department")
    to_account = forms.ModelChoiceField(queryset=Vendor.objects.all(), empty_label="Select a Vendor")
    
    class Meta:
        model = Payment
        fields = (
            'from_account','to_account','description',
            'invoice','amount',
            )

    def __init__(self, *args,**kwargs):
        super(PaymentForm, self).__init__(*args,**kwargs)
        self.fields['from_account'].widget.attrs.update({'class': 'form-control'})
        self.fields['to_account'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({
            'class': 'form-control', 
            'rows':5, 
            'placeholder':'Please describe the item!'
            })
        self.fields['invoice'].widget.attrs.update({'class': 'form-control'})
        self.fields['amount'].widget.attrs.update({'class': 'form-control'})

class ReceiveForm(forms.ModelForm):
    
    to_account = forms.ModelChoiceField(queryset=Company.objects.all(), empty_label="Select your department")
    from_account = forms.ModelChoiceField(queryset=Customer.objects.all(), empty_label="Select a Customer")
    
    class Meta:
        model = Receive
        fields = (
            'to_account','from_account','description',
            'invoice','amount',
            )

    def __init__(self, *args,**kwargs):
        super(ReceiveForm, self).__init__(*args,**kwargs)
        self.fields['to_account'].widget.attrs.update({'class': 'form-control'})
        self.fields['from_account'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({
            'class': 'form-control', 
            'rows':5, 
            'placeholder':'Please describe the item!'
            })
        self.fields['invoice'].widget.attrs.update({'class': 'form-control'})
        self.fields['amount'].widget.attrs.update({'class': 'form-control'})