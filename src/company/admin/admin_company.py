from django.contrib import admin
from src.company.const import COMPANIES_INITIAL_DATA
from src.company.models import Company, Address, Owner


class CompanyAdmin(admin.ModelAdmin):

    fields = ['title', 'parent_company', 'owners', 'logo', 'is_active',

              'description', 'address', 'account_type', ]

    def save_model(self, request, obj, form, change):
        obj.username = request.user
        print("yes")
        return super(CompanyAdmin, self).save_model(request, obj, form, change)

    @staticmethod
    def initial_data():
        for index, com in enumerate(COMPANIES_INITIAL_DATA):
            company = Company.objects.filter(id=com['id']).first()
            if not company:
                user = User.objects.get(email='root@root.com')
                company = Company(**com)
                company.user = user
                company.save(force_insert=True)
            else:
                company.title = com['title']
                company.parent_company = com['parent_company']
                company.description = com['description']
                company.address = com['address']
                company.account_type = com['account_type']
                company.save(force_update=True)
                company.owners.set(com['owners'])
                company.save()
                company.logo = com['logo']
                company.save()
                company.is_active = com['is_active']
                company.save()
                company.save()
