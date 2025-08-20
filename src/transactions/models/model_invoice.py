from django.db import models
from src.company.models import Company
from src.accounts.models import Customer, Vendor


INVOICE_STATUS = (
    ('pending', 'PENDING'),
    ('invoked', 'INVOKED'),
    ('paid', 'PAID')
)

PAYMENT_METHOD = (
    ('cash', 'CASH'),
    ('Credit Card', 'CREDIT CARD'),
    ('Cheque', 'CHEQUE')
)

class Invoice(models.Model):
    account = models.ForeignKey(Company, on_delete=models.CASCADE, default=1)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    # sale_query = models.QuerySet(Sale.objects.filter(customer=customer))
    # total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    note = models.TextField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    payment_term = models.CharField(
        max_length=60, choices=PAYMENT_METHOD, default='cash'
    )
    total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    status = models.CharField(
        max_length=30, choices=INVOICE_STATUS, default='pending')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __init__(self, *args, **kwargs):
        super(Invoice, self).__init__(*args, **kwargs)

    def __str__(self):
        return f'{self.id} - {self.customer}'

    def get_absolute_url(self):
        return reverse('sales_invoice_detail', kwargs={'pk': self.pk})

    @property
    def get_sale_items(self):
        return InvoiceItem.objects.filter(invoice=self)

    @property
    def get_total_price(self):
        items = InvoiceItem.objects.filter(invoice=self)
        total = 0
        for item in items:
            total += item.total
        return total

    def get_update_url(self):
        return reverse('sales_invoice_update', args=(self.pk,))

    def pay(self):
        return reverse('sales_invoice_pay', args=(self.pk,))
