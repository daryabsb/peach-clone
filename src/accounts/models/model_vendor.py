from django.db import models
from src.core.base import CVbase
from src.finances.models import AccountSub



class Vendor(CVbase):
    account_type = models.ForeignKey(
        AccountSub, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def get_account_sub(self):
        return self.account_type

    def save(self, *args, **kwargs):
        if not self.account_type:
            a_sub = AccountSub.objects.get(title='Account Payable')
            self.account_type = a_sub
            print(self.account_type)
            # self.total = self.unit_price * self.quantity
        super(Vendor, self).save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse('company-detail', kwargs={'pk': self.pk})

