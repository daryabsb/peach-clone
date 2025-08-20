from django.db import models

DEPRECIATION_CHOICES = [
    (1, 'Depreciation'),
    (2, 'Prepaid'),
    (3, 'Supplies')
]

# D = Depreciation - S = Supplies - P = Prepaid
class DSP(models.Model):
    title = models.CharField(max_length=60, null=True, blank=True)
    depreciation_choices = models.PositiveIntegerField(
        choices=DEPRECIATION_CHOICES)
    # year_of_purchase = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    lifespan = models.PositiveIntegerField()

    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.created}'

    # def save(self, *args, **kwargs):
    #     now = datetime.datetime.now()
    #     self.year_of_purchase = now.year
    #     super(Sale, self).save(*args, **kwargs)
