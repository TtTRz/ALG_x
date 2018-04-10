from django.shortcuts import render_to_response ,get_object_or_404
from . models import Item,ItemType
from django.core.paginator import Paginator
# Create your views here.

# 商品列表
def item_list(request):
    items_all_list = Item.objects.all()#全部商品
    paginator = Paginator(items_all_list, 10)  # 每十个商品进行分页
    page_num =request.GET.get('page',1)#获取url的页码参数（‘GET请求’）
    page_of_items =paginator.get_page(page_num)#自动识别page系以及是否为有效数字，若不是则返回第一页
    context = {}

    context['page_of_items'] = page_of_items#该页面的所有商品
    context['item_types'] = ItemType.objects.all()
    #返回所有的商品类型
    return render_to_response('item/item_list.html',context)
# 商品详细内容
def  item_detail(request,item_pk):
    context = {}
    context ['item'] = get_object_or_404(Item, pk =item_pk) #如果没有该商品目录则返回404
    return render_to_response('item/item_detail.html',context)


#商品类型分类（同一类放在一起）
def  items_with_type(request,items_type_pk):

    context = {}
    item_type = get_object_or_404(ItemType,pk = items_type_pk)
    context['items'] = Item.objects.filter(item_type = item_type)
    context['item_type'] = item_type
    context['item_types'] = ItemType.objects.all()
    return render_to_response('item/items_with_type.html',context)