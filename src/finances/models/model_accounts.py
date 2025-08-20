from django.db import models
from src.core.base import AccountTemplate





ACCOUNT_SECTIONS = (
    ("Assets", "ASSETS"),
    ("Liabilities", "LIABILITIES"),
    ("Equity", "EQUITY"),
    ("Revenue", "REVENUE"),
    ("Expense", "EXPENSE"),
)


class AccountMain(AccountTemplate):
    # company = models.ForeignKey(Company, on_delete=models.CASCADE)
    account_section = models.CharField(max_length=30, choices=ACCOUNT_SECTIONS)

    def __str__(self):
        return f'{self.title} ({self.account_section})'

    # def get_absolute_url(self):
    #     return reverse('company-detail', kwargs={'pk': self.pk})


class AccountSub(AccountTemplate):
    main = models.ForeignKey('AccountMain', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} ({self.main})'

    # def get_absolute_url(self):
    #     return reverse('company-detail', kwargs={'pk': self.pk})
