
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ModelForm, widgets
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from core.models import User

"""
TEMPLATE FORM SELECT

class SomeForm(forms.Form):
    customer = forms.ChoiceField(label=u'Customer')

    def __init__(self, *args, **kwargs):
        super(SomeForm, self).__init__(*args, **kwargs)
        self.fields['customer'].choices = [(e.id, e.customer) for e in Customers.objects.all()]


"""


class SaleForm(forms.Form):
    customer = forms.ModelMultipleChoiceField(queryset=None)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].queryset = Customer.objects.all()


class SaleForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(TransactionForm, self).__init__(*args, **kwargs)
        self.
        self.fields['username'].widget = widgets.ChoiceWidget(attrs={'placeholder': "Selece an Option"}, choices=...) TextInput(
            attrs={'placeholder': "username", "class": "form-control"})
        self.fields['password'].widget = widgets.PasswordInput(
            attrs={'placeholder': "password", "class": "form-control"})

    department = models.ForeignKey('Company', on_delete=models.CASCADE)
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)
    # amount = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    # credit_account
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(
        max_digits=9, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    note = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        # self.fields['username'].widget = widgets.TextInput(
        #     attrs={'placeholder': "username", "class": "form-control form-control-line"})
        self.fields['email'].widget = widgets.EmailInput(
            attrs={'placeholder': "email", "class": "form-control form-control-line"})
        self.fields['password1'].widget = widgets.PasswordInput(
            attrs={'placeholder': "password", "class": "form-control form-control-line"})
        self.fields['password2'].widget = widgets.PasswordInput(
            attrs={'placeholder': "repeat password", "class": "form-control form-control-line"})

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("The email already exists.")
        return email

    class Meta:
        model = User
        fields = ("email", "password")
