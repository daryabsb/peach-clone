from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import DecimalField
from django.db.models import IntegerField
from django.db.models import PositiveSmallIntegerField
from django.db.models import TextField
from django_extensions.db.fields import AutoSlugField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields
from contact.models import Customer
from product.models import ProductVariant
from django.utils import timezone
class Invoice(models.Model):

    # Fields
    slug = extension_fields.AutoSlugField(populate_from='id', blank=True)
    created = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now)
    rate = models.PositiveSmallIntegerField()
    btype_choices=(
            ("Cash","Cash"),
            ("Metal","Metal")
        )
    itype_choices=(
        ("Cash","Cash"),
        ("Credit","Credit")
    )
    balancetype = models.CharField(max_length=30,choices=btype_choices,default="Cash")
    paymenttype = models.CharField(max_length=30,choices=itype_choices,default="Cash")
    balance = models.DecimalField(max_digits=10, decimal_places=3)
    status = models.CharField(max_length=30)

    # Relationship Fields
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,related_name="invoicee"
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('sales_invoice_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('sales_invoice_update', args=(self.slug,))


class InvoiceItem(models.Model):

    # Fields
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    touch = models.PositiveSmallIntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    is_return = models.BooleanField(default=False,verbose_name='Return')
    quantity = models.IntegerField()
    makingcharge=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    # Relationship Fields
    product = models.ForeignKey(
        ProductVariant,
        on_delete=models.CASCADE, related_name="item"
    )
    invoice = models.ForeignKey(
        'sales.Invoice',
        on_delete=models.CASCADE, related_name="invoice"
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('sales_invoiceitem_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('sales_invoiceitem_update', args=(self.pk,))


class Receipt(models.Model):

    # Fields
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    type = models.CharField(max_length=30,verbose_name='Metal/Gold')
    total = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=100)

    # Relationship Fields
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE, related_name="receivedfrom"
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('sales_receipt_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('sales_receipt_update', args=(self.slug,))
