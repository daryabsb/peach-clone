from django.contrib import admin
from src.finances.models import AccountMain, AccountSub


admin.site.register(AccountMain)
admin.site.register(AccountSub)