from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from .models import User, Company, Owner, AccountMain, AccountSub, Item, Purchase, Sale, Customer, Vendor


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important Dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        ('None', {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )


class CompanyAdmin(admin.ModelAdmin):

    fields = ['title', 'parent_company', 'owners',
              'description', 'address', 'account_type', ]

    def save_model(self, request, obj, form, change):
        obj.username = request.user
        print("yes")
        return super(CompanyAdmin, self).save_model(request, obj, form, change)


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Owner)
admin.site.register(AccountMain)
admin.site.register(AccountSub)
admin.site.register(Item)
admin.site.register(Purchase)
admin.site.register(Sale)
admin.site.register(Customer)
admin.site.register(Vendor)
