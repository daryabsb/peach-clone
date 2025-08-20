from django.db import models
from src.finances.models import AccountSub

# Create your models here.


"""
For IncomeStatement:
1. If a payment transaction  is done for an expense the account of the expense
    will be recorded to the income statement
rent    $500    [operating expense]bv
"""

MODEL_CHOICES = (
    ('Purchase', 'PURCHASE'),
    ('Sale', 'SALE'),
    ('Payment', 'PAYMENT'),
    ('Receive', 'RECEIVE'),
)


class BalanceSheet(models.Model):
    """
    account_name = models.CharField(max_length=200)
    """
    pass


class IncomeStatement(models.Model):

    model = models.CharField(max_length=10, choices=MODEL_CHOICES)
    model_id = models.PositiveIntegerField()
    account = models.ForeignKey(AccountSub, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.model} - {self.model_id} ({self.account})'




class Expense(models.Model):
    pass


class Revenue(models.Model):
    pass

