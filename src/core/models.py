from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from io import BytesIO
from datetime import datetime  # Correct import
from django.apps import apps
from src.company.models import Company, Address
from src.core.base import AccountTemplate
from src.finances.models import AccountSub
from src.accounts.models import Customer, Vendor



from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

from django.conf import settings

from django.db.models import Sum


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        # Creates and save a new user
        if not email:
            raise ValueError('Users must have an email address!')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        # Creates and save a new superuser
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user




class Account(models.Model):
    pass
    """
    1 Balance Sheet
    """




    # def get_absolute_url(self):
    #     return reverse('company-detail', kwargs={'pk': self.pk})


# TANSACTION_CATEGORY = (
#     ("Purchase", "ASSETS"),
#     ("Sale", "LIABILITIES"),
#     ("Payment", "EQUITY"),
#     ("Receive", "REVENUE"),
# )

"""
MODELS: CUSTOMER,   VENDOR, SUPPLIER
"""





""" END """


# class TransactionType(models.Model):

#     debit_account = models.ForeignKey(Company, on_delete=models.CASCADE)
#     credit_account = models.CharField(max_length=30, blank=True, null=True)
#     # amount = models.IntegerField(default=0)
#     description = models.TextField(blank=True, null=True)
# credit_account

"""
    Purchase
    Sale
    Payment
    Receive
    """




