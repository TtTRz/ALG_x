from django.shortcuts import render
from item.models import Item,ItemType

# Create your views here.

def index(request):
    types = ItemType.objects.all()
    item = [Item.objects.filter(item_type=it) for it in types]
    type_name = [name.type_name for name in types]
    return render(request, 'ALG_web/home.html',{'type' : item})

