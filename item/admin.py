from django.contrib import admin
from .models import ItemType,Item
# Register your models here.
@ admin.register(ItemType)
class ItemTypeAdmin(admin.ModelAdmin):
    list_display = ('id','type_name')
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin ):
    list_display = ('id','title','item_type','pic','price','author','get_read_num','created_time','last_updated_time')