from django.shortcuts import render_to_response ,get_object_or_404
from . models import Item,ItemType
# Create your views here.

# 商品列表
def item_list(request):
    context = {}
    context['items'] = Item.objects.all()#返回所有商品的信息

    return render_to_response('item/item_list.html',context)
# 商品详细内容
def  item_detail(request,item_pk):
    context = {}
    context ['item'] = get_object_or_404(Item, pk =item_pk) #如果没有该商品目录则返回404
    return render_to_response('item/item_detail.html',context)


#商品类型分类（同一类放在一起）
def  items_with_type(request,items_with_type):
    context = {}
    item_type = get_object_or_404(ItemType,pk = items_with_type)
    context['items'] = Item.objects.filter(item_type = item_type)
    context['item_type'] = item_type
    return render_to_response('item/items_with_type.html',context)