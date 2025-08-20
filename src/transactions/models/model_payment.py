from django.db import models
from src.company.models import Company
from src.accounts.models import Vendor

PAYMENT_METHOD = (
    ('cash', 'CASH'),
    ('Credit Card', 'CREDIT CARD'),
    ('Cheque', 'CHEQUE')
)


class Payment(models.Model):

    from_account = models.ForeignKey(
        Company, on_delete=models.CASCADE, default=1)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    purchase_invoice = models.ForeignKey(
        'PurchaseInvoice', on_delete=models.CASCADE, null=True, blank=True)
    payment_method = models.CharField(
        max_length=20, choices=PAYMENT_METHOD, default='cash')
    description = models.TextField(null=True, blank=True)
    total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.total} to {self.vendor}'

    @property
    def get_account_sub(self):
        return self.vendor.account_type

    def get_total_list_price(self):
        total = self.objects.all().aggregate(Sum('amount'))
        print(total)
        return total

    # def get_absolute_url(self):
    #     return reverse('company-detail', kwargs={'pk': self.pk})
