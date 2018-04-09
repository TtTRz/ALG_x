from django.shortcuts import render_to_response ,get_object_or_404
from . models import Item,ItemType
# Create your views here.

# 商品列表
def item_list(request):
    content = {}
    content['items'] = Item.objects.all()#返回所有商品的信息

    return render_to_response('item/item_list.html',content)
# 商品详细内容
def item_detail(request,item_pk):
    content = {}
    content ['item'] = get_object_or_404(Item, pk =item_pk) #如果没有该商品目录则返回404
    return render_to_response('item/item_detail.html',content)