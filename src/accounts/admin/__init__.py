from django.contrib import admin
from src.accounts.models import User, Customer, Vendor


from src.accounts.admin.admin_user import UserAdmin


admin.site.register(User, UserAdmin)
admin.site.register(Customer)
admin.site.register(Vendor)
