from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import Item, Purchase, Sale, Vendor, Customer, Payment, Receive, Depretiation, Journal, AccountSub
# Payment,
# Receive


@receiver(post_save, sender=Purchase)
def update_vendor_balance_on_purchase(sender, instance, created, **kwargs):
    if created:
        vendor = Vendor.objects.get(name=instance.vendor)
        print('created - Purchase')
        print(vendor.balance)
        print(instance.total)
        vendor.balance += instance.total
        vendor.save()


@receiver(post_save, sender=Sale)
def update_customer_balance_on_sale(sender, instance, created, **kwargs):
    if created:
        customer = Customer.objects.get(name=instance.customer)
        print('created - Sale')
        print(customer.balance)
        print(instance.total)
        customer.balance += instance.total
        customer.save()


@receiver(post_save, sender=Payment)
def update_vendor_balance_on_pay(sender, instance, created, **kwargs):
    if created:
        vendor = Vendor.objects.get(name=instance.to_account)
        print('created - Payment')
        print(vendor.balance)
        print(instance.amount)
        vendor.balance -= instance.amount
        vendor.save()


@receiver(post_save, sender=Receive)
def update_customer_balance_on_receive(sender, instance, created, **kwargs):
    if created:
        customer = Customer.objects.get(name=instance.from_account)
        print('created - Receive')
        print(customer.balance)
        print(instance.amount)
        customer.balance -= instance.amount
        customer.save()


@receiver(post_save, sender=Item)
def update_customer_balance_on_depretiation(sender, instance, created, **kwargs):
    if created:
        item_dep = Depretiation.objects.create(
            item=instance.item,
            rate=instance.ite_depretiation)
        print('created - Item')
        item_dep.save()


@receiver(post_save, sender=Purchase)
def add_journal_purchase(sender, instance, created, **kwargs):
    if created:
        debit_account = instance.get_account_sub
        credit_account = instance.vendor.get_account_sub
        model_name = 'Purchase'
        model_id = instance.pk

        journal = Journal.objects.create(
            dr_account=debit_account,
            cr_account=credit_account,
            sender_model=model_name,
            model_id=model_id,
            amount=instance.total
        )

        print('created - Purchase - Journal')
        journal.save()


@receiver(post_save, sender=Sale)
def add_journal_sale(sender, instance, created, **kwargs):
    if created:
        debit_account = instance.get_account_sub
        credit_account = instance.customer.get_account_sub
        model_name = 'Sale'
        model_id = instance.pk

        cash = AccountSub.objects.get(title='Cash')
        account_receiveable = AccountSub.objects.get(title='Account Receivable')

        account_receiveable.cr += instance.amount
        account_receiveable.save() 

        journal = Journal.objects.create(
            dr_account=debit_account,
            cr_account=credit_account,
            sender_model=model_name,
            model_id=model_id,
            amount=instance.total
        )

        print('created - Sale - Journal')
        journal.save()


@receiver(post_save, sender=Payment)
def add_journal_payment(sender, instance, created, **kwargs):
    if created:
        if instance.payment_method == 'cash':
            cash = AccountSub.objects.get(title='Cash')
            debit_account = instance.to_account.get_account_sub
            credit_account = cash
            model_name = 'Payment'
            model_id = instance.pk

            cash.dr -= instance.amount
            cash.save()

            journal = Journal.objects.create(
                dr_account=debit_account,
                cr_account=credit_account,
                sender_model=model_name,
                model_id=model_id,
                amount=instance.amount
            )

            print('created - Payment - Journal')
            journal.save()


@receiver(post_save, sender=Receive)
def add_journal_receive(sender, instance, created, **kwargs):
    if created:
        if instance.payment_method == 'cash':
            cash = AccountSub.objects.get(title='Cash')
            account_receiveable = AccountSub.objects.get(title='Account Receivable')
            debit_account = cash
            credit_account = instance.from_account.get_account_sub
            model_name = 'Receive'
            model_id = instance.pk

            cash.cr += instance.amount
            cash.save()
            

            account_receiveable.dr -= instance.amount
            account_receiveable.save()

            journal = Journal.objects.create(
                dr_account=debit_account,
                cr_account=credit_account,
                sender_model=model_name,
                model_id=model_id,
                amount=instance.amount
            )

            print('created - Receive - Journal')
            journal.save()
