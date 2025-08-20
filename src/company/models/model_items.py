from django.db import models
from src.core.base import AccountTemplate



class Item(AccountTemplate):
    address = models.ForeignKey(
        "Address", on_delete=models.CASCADE, blank=True, null=True
    )
    item_depretiation = models.ForeignKey('DSP', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} - {self.account_sub}'