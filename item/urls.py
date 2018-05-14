from django.urls import path

from .import views

app_name = 'item'
urlpatterns = [

    path('<int:item_pk>',views.item_detail,name='item_detail'),
    #localhost:8000/item/(商品编号)
    path('list/digital/',views.item_list_digital, name='item_list_digital'),
    path('list/clothing/', views.item_list_clothing, name='item_list_clothing'),
    path('list/groceries/', views.item_list_groceries, name='item_list_groceries'),

    #localhost：8000/item/list
    path("type/<int:items_type_pk>",views.items_with_type,name = 'items_with_type'),
    path("search/",views.search,name='search'),
    path("add/",views.item_add,name='item_add')
]