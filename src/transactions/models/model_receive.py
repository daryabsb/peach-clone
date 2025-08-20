from django.db import models
from src.company.models import Company
from src.accounts.models import Customer

PAYMENT_METHOD = (
    ('cash', 'CASH'),
    ('Credit Card', 'CREDIT CARD'),
    ('Cheque', 'CHEQUE')
)


class Receive(models.Model):

    to_account = models.ForeignKey(
        Company, on_delete=models.CASCADE, default=1)
    from_account = models.ForeignKey(Customer, on_delete=models.CASCADE)
    invoice = models.ForeignKey(
        'Invoice', on_delete=models.CASCADE,  null=True, blank=True)
    # invoice = models.CharField(max_length=60, null=True, blank=True)
    payment_method = models.CharField(
        max_length=20, choices=PAYMENT_METHOD, default='cash')
    description = models.TextField(null=True, blank=True)
    amount = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk} - {self.amount} from {self.from_account}'

    @property
    def get_account_sub(self):
        return self.from_account.account_type

    def get_absolute_url(self):
        return reverse('sales_receive_detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('sales_receive_update', args=(self.pk,))
# REPORTS

