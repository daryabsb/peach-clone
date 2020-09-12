from django.db import models
from django.urls import reverse
from django.utils import timezone


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

from django.conf import settings

from django.db.models import Sum


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        # Creates and save a new user
        if not email:
            raise ValueError('Users must have an email address!')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        # Creates and save a new superuser
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(PermissionsMixin, AbstractBaseUser):
    # Custom user model supports email instead of username
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'


ACCOUNT_TYPE = (
    ('accrual', 'ACCRUAL'),
    ('cash', 'CASH'),
)


class Company(models.Model):
    user = models.ForeignKey('User', null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    parent_company = models.ForeignKey(
        'Company', related_name='Parent', on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    owners = models.ManyToManyField('Owner')
    address = models.CharField(max_length=200)
    account_type = models.CharField(
        max_length=20,  default='accrual', choices=ACCOUNT_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    """
    1 IK    -
    2 Fig   IK
    3 Biza  IK
    """

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('company-detail', kwargs={'pk': self.pk})


class Owner(models.Model):
    name = models.CharField(max_length=200)
    share = models.DecimalField(max_digits=2, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('company-detail', kwargs={'pk': self.pk})


class Account(models.Model):
    pass
    """
    1 Balance Sheet
    """


class AccountTemplate(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    dr = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    cr = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - dr: {self.dr}'


ACCOUNT_SECTIONS = (
    ("Assets", "ASSETS"),
    ("Liabilities", "LIABILITIES"),
    ("Equity", "EQUITY"),
    ("Revenue", "REVENUE"),
    ("Expense", "EXPENSE"),
)


class AccountMain(AccountTemplate):
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    account_section = models.CharField(max_length=30, choices=ACCOUNT_SECTIONS)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('company-detail', kwargs={'pk': self.pk})


class AccountSub(AccountTemplate):
    main = models.ForeignKey('AccountMain', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('company-detail', kwargs={'pk': self.pk})


class Item(AccountTemplate):
    account_sub = models.ForeignKey('AccountSub', on_delete=models.CASCADE)
    ite_depretiation = models.DecimalField(
        max_digits=2, decimal_places=2, default=0.00)
    unit = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('company-detail', kwargs={'pk': self.pk})


# TANSACTION_CATEGORY = (
#     ("Purchase", "ASSETS"),
#     ("Sale", "LIABILITIES"),
#     ("Payment", "EQUITY"),
#     ("Receive", "REVENUE"),
# )

"""
MODELS: CUSTOMER,   VENDOR, SUPPLIER
"""


class CVbase(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    balance = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    note = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Customer(CVbase):

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('company-detail', kwargs={'pk': self.pk})


class Vendor(CVbase):

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('company-detail', kwargs={'pk': self.pk})


""" END """


# class TransactionType(models.Model):

#     debit_account = models.ForeignKey('Company', on_delete=models.CASCADE)
#     credit_account = models.CharField(max_length=30, blank=True, null=True)
#     # amount = models.IntegerField(default=0)
#     description = models.TextField(blank=True, null=True)
# credit_account

"""
    Purchase
    Sale
    Payment
    Receive
    """


class Purchase(models.Model):
    department = models.ForeignKey('Company', on_delete=models.CASCADE)
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)
    # amount = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    # credit_account
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
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

    def get_total_list_price(self):
        total = self.objects.all().aggregate(Sum('total'))
        # tot Purchase.objects.filter(
        #     credit_account=vendor).aggregate(Sum('total'))
        return total

    # def get_absolute_url(self):
    #     return reverse('company-detail', kwargs={'pk': self.pk})


class Sale(models.Model):

    department = models.ForeignKey(
        'Company', on_delete=models.CASCADE, default=1)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(
        max_digits=9, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    note = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.total = self.unit_price * self.quantity
        super(Sale, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.item} - {self.total} to {self.customer}'

    def get_total_list_price(self):
        total = self.objects.all().aggregate(Sum('total'))
        # tot Purchase.objects.filter(
        #     credit_account=vendor).aggregate(Sum('total'))
        return total

    # def get_absolute_url(self):
    #     return reverse('company-detail', kwargs={'pk': self.pk})


class Payment(models.Model):

    from_account = models.ForeignKey(
        'Company', on_delete=models.CASCADE, default=1)
    to_account = models.ForeignKey('Vendor', on_delete=models.CASCADE)
    invoice = models.CharField(max_length=60, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    amount = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.amount} to {self.to_account}'

    def get_total_list_price(self):
        total = self.objects.all().aggregate(Sum('amount'))
        print(total)
        return total

    # def get_absolute_url(self):
    #     return reverse('company-detail', kwargs={'pk': self.pk})


class Receive(models.Model):

    to_account = models.ForeignKey(
        'Company', on_delete=models.CASCADE, default=1)
    from_account = models.ForeignKey('Customer', on_delete=models.CASCADE)
    invoice = models.CharField(max_length=60, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    amount = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.amount} from {self.from_account}'

    # def get_absolute_url(self):
    #     return reverse('company-detail', kwargs={'pk': self.pk})

# REPORTS


class Invoice(models.Model):
    account = models.ForeignKey('Company', on_delete=models.CASCADE)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)

    sale_items = models.ManyToManyField(Sale)
    # sale_query = models.QuerySet(Sale.objects.filter(customer=customer))
    # total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    note = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.created}'

    # def save(self, *args, **kwargs):
    #     self.total = self.calculate_total()
    #     super(Invoice, self).save(*args, **kwargs)

    # def calculate_total(self):
    #     return sum(item.total for item in self.sale_items.all())


class Depretiation(models.Model):
    item = models.OneToOneField('Item', on_delete=models.CASCADE)
    rate = models.DecimalField(max_digits=2, decimal_places=2, default=0.00)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.item} - {self.rate}'


class BalanceSheet(models.Model):
    """
    account_name = models.CharField(max_length=200)
    """
    pass


class IncomeStatement(models.Model):
    pass
