from django.contrib import admin
from src.company.const import COMPANIES_INITIAL_DATA
from src.company.models import Company, Address, Owner
from src.accounts.models import User


class CompanyAdmin(admin.ModelAdmin):

    fields = ['title', 'parent_company', 'owners', 'logo', 'is_active',
              'description', 'address', 'account_type', ]

    # def save_model(self, request, obj, form, change):
    #     obj.username = request.user
    #     print("yes")
    #     return super(CompanyAdmin, self).save_model(request, obj, form, change)

    @staticmethod
    def initial_data():
        for index, com in enumerate(COMPANIES_INITIAL_DATA):
            company = Company.objects.filter(id=com['id']).first()
            if not company:
                user = User.objects.get(email='root@root.com')
                if com['parent_company']:
                    parent_company = Company.objects.filter(
                        id=com['parent_company']).first()
                    if parent_company:
                        com['parent_company'] = parent_company
                    else:
                        com['parent_company'] = None
                company = Company(**com)
                company.user = user
                company.save(force_insert=True)
            else:
                company.title = com['title']
                company.save(force_update=True)
