from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from read_statistics.utils import read_statistics_once_read
from .models import Item, ItemType


# Create your views here.


def get_item_list_common_date(items_all_list, request):
    paginator = Paginator(items_all_list, settings.EACH_PAGE_ITEMS_NUMBER)
    # 每5个商品进行分页
    page_num = request.GET.get('page', 1)
    # 获取url的页码参数（‘GET请求’）
    page_of_items = paginator.get_page(page_num)
    # 自动识别page系以及是否为有效数字，若不是则返回第一页
    current_page_num = page_of_items.number  # 获取当前页码
    # 页码控制在1-所有页码之间，获取当前页码前后两页的范围
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + \
                 list(range(current_page_num, min(paginator.num_pages, current_page_num + 2) + 1))

    # 页码间加上省略号标记,当前页面首尾页超过两页则中间页码为省略号标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    # 加上首页和尾页，方便一键返回首尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    # 获取分类商品的对应商品数量
    item_types = ItemType.objects.all()
    # 获取各个分类的数量
    item_types_list = []
    for item_type in item_types:
        item_type.item_count = Item.objects.filter(item_type=item_type).count()
        item_types_list.append(item_type)

    context = {}
    context['page_of_items'] = page_of_items  # 该页面的所有商品
    context['item_types'] = item_types_list
    context['page_range'] = page_range
    # 包括当前页面的前后两页页码
    context['items'] = page_of_items.object_list

    return context


# 商品列表
def item_list(request):
    items_all_list = Item.objects.all()  # 全部商品
    context = get_item_list_common_date(items_all_list, request)
    return render(request, 'item/item_list1.html', context)


# 商品详细内容


# 商品类型分类（同一类放在一起）
def items_with_type(request, items_type_pk):
    item_type = get_object_or_404(ItemType, pk=items_type_pk)
    items_all_list = Item.objects.filter(item_type=item_type)  # 全部商品
    context = get_item_list_common_date(items_all_list, request)
    context['item_type'] = item_type

    return render(request, 'item/items_with_type.html', context)


def item_detail(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    read_cookie_key = read_statistics_once_read(request, item)
    item_content_type = ContentType.objects.get_for_model(item)
    context = {}
    context['item'] = get_object_or_404(Item, pk=item_pk)  # 如果没有该商品目录则返回404
    context['previous_item'] = Item.objects.filter(created_time__gt=item.created_time).last()
    # 获取当前商品的创建时间，并以这个时间进行比较，大于该时间的最后一个商品则为上一个
    context['next_item'] = Item.objects.filter(created_time__lt=item.created_time).first()
    # h同样方法获取下一个商品
    response = render(request, 'item/item_detail1.html', context)  # 响应
    response.set_cookie(read_cookie_key, 'true')  # 阅读cookie标记
    return response
