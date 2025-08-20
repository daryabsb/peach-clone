from django.db import models
from src.company.models import Company, Item
from src.accounts.models import Vendor



class Purchase(models.Model):
    department = models.ForeignKey(
        Company, 
        on_delete=models.CASCADE,
        default=1
        )
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    purchase_invoice = models.ForeignKey(
        'PurchaseInvoice', on_delete=models.CASCADE, null=True, blank=True)
    # amount = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    # credit_account
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(
        max_digits=9, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    note = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # def save(self):
    #     return self.unit_price * self.quantity
    def save(self, *args, **kwargs):
        self.total = self.unit_price * self.quantity
        super(Purchase, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.item} - {self.total}'

    @property
    def get_account_sub(self):
        return self.item.account_sub

    def get_total_list_price(self):
        total = self.objects.all().aggregate(Sum('total'))
        # tot Purchase.objects.filter(
        #     credit_account=vendor).aggregate(Sum('total'))
        return total

    # def get_absolute_url(self):
    #     return reverse('company-detail', kwargs={'pk': self.pk})
