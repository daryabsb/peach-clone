from django.contrib import admin
from src.configurations.models import Menu, Item

from mptt.admin import DraggableMPTTAdmin


class ItemInlineAdmin(admin.TabularInline):
    model = Item
    extra=2

class MenuAdmin(admin.ModelAdmin):
    inlines = [ItemInlineAdmin]
    prepopulated_fields = {"slug": ("title",)}


class ItemAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title')
    list_display_links = ('indented_title',)


admin.site.register(Menu, MenuAdmin)
admin.site.register(Item,ItemAdmin)
