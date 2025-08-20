from django.contrib import admin



class CompanyAdmin(admin.ModelAdmin):

    fields = ['title', 'parent_company', 'owners',
              'description', 'address', 'account_type', ]

    def save_model(self, request, obj, form, change):
        obj.username = request.user
        print("yes")
        return super(CompanyAdmin, self).save_model(request, obj, form, change)