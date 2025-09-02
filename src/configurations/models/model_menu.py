from django.db import models
from django.utils.text import slugify

from django.conf import settings
from mptt.models import MPTTModel, TreeForeignKey

class Menu(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,unique=True, null=True)
    access_level = models.SmallIntegerField(default=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    
    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Item(MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    menu = models.ForeignKey("Menu", on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255, blank=False)
    item_id = models.IntegerField(null=True, blank=True)
    type =  models.CharField(max_length=255, blank=True,null=True)
    link = models.CharField(max_length=255, blank=True,default="")
    description = models.TextField(null=True,blank=True)
    attributes = models.JSONField(default=dict, null=True, blank=True)

    order = models.IntegerField(null=True,default=0)
    created = models.DateTimeField(auto_now_add=True) #Automatically set the field to now when the object is first created.
    updated = models.DateTimeField(auto_now=True) #Automatically set the field to now every time the object is saved.

    class MPTTMeta:
        verbose_name = "Item"
        verbose_name_plural = "Items"
        level_attr = 'mptt_level'
        order_insertion_by = ['order']

    def __str__(self):
        return self.title