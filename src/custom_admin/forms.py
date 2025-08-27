from django import forms
from django.contrib.auth.forms import AuthenticationForm
from src.accounts.models import User
from src.company.models import Company, Item
from src.transactions.models import Invoice, Purchase, Sale, Payment, Receive


class CustomAdminAuthForm(AuthenticationForm):
    """Custom authentication form for the admin interface"""
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class CompanyAdminForm(forms.ModelForm):
    """Custom form for Company model in admin"""
    class Meta:
        model = Company
        fields = ['title', 'parent_company', 'owners', 'logo', 'is_active',
                  'description', 'address', 'account_type']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'account_type': forms.Select(attrs={'class': 'form-control'}),
        }


class ItemAdminForm(forms.ModelForm):
    """Custom form for Item model in admin"""
    class Meta:
        model = Item
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class InvoiceAdminForm(forms.ModelForm):
    """Custom form for Invoice model in admin"""
    class Meta:
        model = Invoice
        fields = '__all__'
        widgets = {
            'note': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'due_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'payment_term': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class PurchaseAdminForm(forms.ModelForm):
    """Custom form for Purchase model in admin"""
    class Meta:
        model = Purchase
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class SaleAdminForm(forms.ModelForm):
    """Custom form for Sale model in admin"""
    class Meta:
        model = Sale
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class PaymentAdminForm(forms.ModelForm):
    """Custom form for Payment model in admin"""
    class Meta:
        model = Payment
        fields = '__all__'


class ReceiveAdminForm(forms.ModelForm):
    """Custom form for Receive model in admin"""
    class Meta:
        model = Receive
        fields = '__all__'