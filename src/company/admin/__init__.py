from django.contrib import admin

from src.company.models import Company, Address, Owner, Item, DSP


from .admin_company import CompanyAdmin

admin.site.register(Company, CompanyAdmin)
admin.site.register(Address)
admin.site.register(Owner)
admin.site.register(Item)
admin.site.register(DSP)

