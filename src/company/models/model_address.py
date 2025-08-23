from django.db import models


class Address(models.Model):
    addr_line1 = models.CharField(max_length=400, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    zipcode = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)

    #latitude = models.FloatField(null=True, blank=True);
    #longitude = models.FloatField(null=True, blank=True);

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.addr_line1}, {self.city}, {self.state}, {self.country}"
