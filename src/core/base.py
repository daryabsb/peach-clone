from django.db import models


class AccountTemplate(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    dr = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    cr = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    balance = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - dr: {self.dr}'
    
    class Meta:
        abstract = True



class CVbase(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    balance = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    note = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True