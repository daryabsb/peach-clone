from django.contrib import admin
from .models import AdminPreference, AdminActivity


@admin.register(AdminPreference)
class AdminPreferenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'updated')
    search_fields = ('name',)


@admin.register(AdminActivity)
class AdminActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'content_type', 'object_id', 'timestamp', 'ip_address')
    list_filter = ('user', 'action', 'content_type', 'timestamp')
    search_fields = ('user__email', 'action')
    date_hierarchy = 'timestamp'