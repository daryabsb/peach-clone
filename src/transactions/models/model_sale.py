from django.db import models
from src.company.models import Company, Item
from src.accounts.models import Customer



class Sale(models.Model):

    department = models.ForeignKey(
        Company, on_delete=models.CASCADE, default=1)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    invoice = models.ForeignKey(
        'Invoice', on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(
        max_digits=9, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    balance = models.DecimalField(
        max_digits=10, decimal_places=3, default=0.00)
    status = models.CharField(max_length=30, default='unpaid')
    note = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.total = self.unit_price * self.quantity
        self.customer = self.invoice.customer
        super(Sale, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.pk} | {self.item} - {self.total} to {self.customer}'

    @property
    def get_account_sub(self):
        return self.item.account_sub

    @property
    def get_total_list_price(self, items):
        total = self.objects.all().aggregate(Sum('total'))
        # tot Purchase.objects.filter(
        #     credit_account=vendor).aggregate(Sum('total'))
        return total


    # def get_absolute_url(self):
    #     return reverse('company-detail', kwargs={'pk': self.pk})

