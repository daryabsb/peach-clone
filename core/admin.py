from django.contrib import admin

from .models import Company, Owner, AccountMain, AccountSub, item, Purchase

# Register your models here.

admin.site.register(Company)
admin.site.register(Owner)
admin.site.register(AccountMain)
admin.site.register(AccountSub)
admin.site.register(item)
admin.site.register(Purchase)

