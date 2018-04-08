from django.contrib import admin
from .models import ItemType, Item

@admin.register(ItemType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')

@admin.register(Item)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'item_type', 'author', 'created_time', 'last_updated_time')
