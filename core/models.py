from django.db import models


class Company(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    owners = models.ManyToManyField('Owner')

    """
    1 IK    -
    2 Fig   IK
    3 Biza  IK
    """

    def __str__(self):
        return self.title


class Owner(models.Model):
    name = models.CharField(max_length=200)
    share = models.DecimalField(max_digits=2, decimal_places=2)

    def __str__(self):
        return self.name


class Account(models.Model):
    pass
    """
    1 Balance Sheet 
    """


class AccountTemplate(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    dr = models.DecimalField(max_digits=9, decimal_places=2)
    cr = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return f'{self.title} - dr: {self.dr}'


ACCOUNT_SECTIONS = (
    ("Assets", "ASSETS"),
    ("Liabilities", "LIABILITIES"),
    ("Equity", "EQUITY"),
    ("Revenue", "REVENUE"),
    ("Expense", "EXPENSE"),
)


class AccountMain(AccountTemplate):
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    account_section = models.CharField(max_length=30, choices=ACCOUNT_SECTIONS)

    def __str__(self):
        return self.title


class AccountSub(AccountTemplate):
    main = models.ForeignKey('AccountMain', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class item(AccountTemplate):
    account_sub = models.ForeignKey('AccountSub', on_delete=models.CASCADE)
    unit = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.title


# TANSACTION_CATEGORY = (
#     ("Purchase", "ASSETS"),
#     ("Sale", "LIABILITIES"),
#     ("Payment", "EQUITY"),
#     ("Receive", "REVENUE"),
# )
class TransactionType(models.Model):

    debit_account = models.ForeignKey('Company', on_delete=models.CASCADE)
    credit_account = models.CharField(max_length=30, blank=True, null=True)
    # amount = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    # credit_account 

    """
    Purchase
    Sale
    Payment
    Receive
    """

class Purchase(TransactionType):
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=9, decimal_places=2)
    total = models.DecimalField(max_digits=9, decimal_places=2)

    # def save(self):
    #     return self.unit_price * self.quantity

    def __str__(self):
        return f'{self.item} - {self.total}'




# REPORTS
class BalanceSheet(models.Model):
    """
    account_name = models.CharField(max_length=200)
    """ 
    pass


class IncomeStatement(models.Model):
    pass
