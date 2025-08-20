from django.db import models

from src.company.models import Company
from src.accounts.models import Vendor

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



class PurchaseInvoice(models.Model):

    # Fields
    # slug = extension_fields.AutoSlugField(populate_from='id', blank=True)
    account = models.ForeignKey(Company, on_delete=models.CASCADE, default=1)
    vendor = models.ForeignKey(
        Vendor,
        on_delete=models.CASCADE,
        related_name="vendors"
    )
    payment_term = models.CharField(
        max_length=60, choices=PAYMENT_METHOD, default='cash'
    )

    # sale_query = models.QuerySet(Sale.objects.filter(customer=customer))
    # total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    note = models.TextField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    
    total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    status = models.CharField(
        max_length=30, choices=INVOICE_STATUS, default='pending')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    # def __unicode__(self):
    #     return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('purchase_invoice_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('purchase_invoice_update', args=(self.pk,))


