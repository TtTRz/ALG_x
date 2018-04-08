from django.shortcuts import get_object_or_404 ,render
from.models import ItemType,Item
from django.db.models import Count
from django.conf import settings
from django.core.paginator import Paginator
from django.contrib.contenttypes.models import ContentType
from read_statistics.utils import read_statistics_once_read
# Create your views here.
def item_list(request):
    items_all_list = Item.objects.all()
    context = {}
    context['items_all_list'] = items_all_list
    return render(request, 'item/item_list.html', context)
def get_item_list_common_data(request, items_all_list):
    paginator = Paginator(items_all_list, settings.EACH_PAGE_BLOGS_NUMBER)
    page_num = request.GET.get('page', 1) # 获取url的页面参数（GET请求）
    page_of_items = paginator.get_page(page_num)
    currentr_page_num = page_of_items.number # 获取当前页码
    # 获取当前页码前后各2页的页码范围
    page_range = list(range(max(currentr_page_num - 2, 1), currentr_page_num)) + \
                 list(range(currentr_page_num, min(currentr_page_num + 2, paginator.num_pages) + 1))
    # 加上省略页码标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')

    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)


    item_dates = Item.objects.dates('created_time', 'month', order="DESC")
    item_dates_dict = {}
    for item_date in item_dates:
        item_count = Item.objects.filter(created_time__year=item_date.year,
                                         created_time__month=item_date.month).count()
        item_dates_dict[item_date] = item_count

    context = {}
    context['items'] = page_of_items.object_list
    context['page_of_items'] = page_of_items
    context['page_range'] = page_range
    context['item_types'] = ItemType.objects.annotate(item_count=Count('blog'))
    context['item_dates'] = item_dates_dict
    return context


def items_with_type(request, item_type_pk):
    item_type = get_object_or_404(ItemType, pk=item_type_pk)
    items_all_list = Item.objects.filter(item_type=item_type)
    context = get_item_list_common_data(request, items_all_list)
    context['item_type'] = item_type
    return render(request, 'item/items_with_type.html', context)


def items_with_date(request, year, month):
    blogs_all_list = Item.objects.filter(created_time__year=year, created_time__month=month)
    context = get_item_list_common_data(request, blogs_all_list)
    context['items_with_date'] = '%s年%s月' % (year, month)
    return render(request, 'item/items_with_date.html', context)

def blog_detail(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    read_cookie_key = read_statistics_once_read(request, item)
    blog_content_type = ContentType.objects.get_for_model(Item)
    # comments = Comment.objects.filter(content_type=blog_content_type, object_id=item.pk)

    context = {}
    context['previous_item'] = Item.objects.filter(created_time__gt=item.created_time).last()
    context['next_blog'] = Item.objects.filter(created_time__lt=item.created_time).first()
    context['blog'] = item
    # context['comments'] = comments
    # context['comment_form'] = CommentForm(initial={'content_type': blog_content_type.model, 'object_id': blog_pk})
    response = render(request, 'blog/blog_detail.html', context) # 响应
    response.set_cookie(read_cookie_key, 'true') # 阅读cookie标记
    return response
