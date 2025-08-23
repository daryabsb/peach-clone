from django.db import models
from src.accounts.models import User
# Create your models here.
ACCOUNT_TYPE = (
    ('accrual', 'ACCRUAL'),
    ('cash', 'CASH'),
)

class Company(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    parent_company = models.ForeignKey(
        'self', related_name='Parent', on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    owners = models.ManyToManyField('Owner')
    address = models.ForeignKey(
        'Address', on_delete=models.CASCADE, blank=True, null=True)
    account_type = models.CharField(
        max_length=20,  default='accrual', choices=ACCOUNT_TYPE)
    is_active = models.BooleanField(default=True)
    logo = models.ImageField(upload_to='company/logo/', blank=True, null=True)


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

