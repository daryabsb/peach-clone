from django.db import models
from src.company.models import Item



class InvoiceItem(models.Model):
    invoice = models.ForeignKey('Invoice', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)

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

    def __str__(self):
        return f'{self.invoice.id} - {self.item.title} ({self.pk})'

    def save(self, *args, **kwargs):
        self.total = self.unit_price * self.quantity
        super(InvoiceItem, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            'sales_invoiceitem_detail',
            kwargs={'pk': self.pk}
        )

    # def calculate_total(self):
    #     return sum(item.total for item in self.sale_items.all())

