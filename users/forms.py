
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import widgets
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from core.models import User


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = widgets.TextInput(
            attrs={'placeholder': "username", "class": "form-control"})
        self.fields['password'].widget = widgets.PasswordInput(
            attrs={'placeholder': "password", "class": "form-control"})


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
