from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import Purchase, Sale, Vendor, Customer, Payment, Receive
# Payment,
# Receive


@receiver(post_save, sender=Purchase)
def update_vendor_balance(sender, instance, created, **kwargs):
    print('Signal Received')
    if created:
        vendor = Vendor.objects.get(name=instance.vendor)
        print('created')
        print(vendor.balance)
        print(instance.total)
        vendor.balance += instance.total
        vendor.save()
    else:
        print('The problem is here')


@receiver(post_save, sender=Sale)
def update_vendor_balance(sender, instance, created, **kwargs):
    print('Signal Received')
    if created:
        customer = Customer.objects.get(name=instance.customer)
        # print('created')
        # print(vendor.balance)
        # print(instance.total)
        customer.balance -= instance.total
        customer.save()


@receiver(post_save, sender=Payment)
def update_vendor_balance(sender, instance, created, **kwargs):
    print('Signal Received')
    if created:
        vendor = Vendor.objects.get(name=instance.vendor)
        print('created')
        print(vendor.balance)
        print(instance.total)
        vendor.balance -= instance.amount
        vendor.save()


@receiver(post_save, sender=Receive)
def update_vendor_balance(sender, instance, created, **kwargs):
    print('Signal Received')
    if created:
        customer = Customer.objects.get(name=instance.from_account)
        customer.balance += instance.amount
        customer.save()
