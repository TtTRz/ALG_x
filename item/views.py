from django.shortcuts import render_to_response ,get_object_or_404
from . models import Item,ItemType
# Create your views here.

# 商品列表
def item_list(request):
    content = {}
    content['items'] = Item.objects.all()

    return render_to_response('item/item_list.html',content)
# 商品详细内容
def item_detail(request,item_pk):
    content = {}
    content ['item'] = get_object_or_404(Item, pk =item_pk)
    return render_to_response('item/item_detail.html',content)