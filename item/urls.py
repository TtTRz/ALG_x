from django.urls import path

from .import views
urlpatterns = [

    path('<int:item_pk>',views.item_detail,name = 'item_detail'),
    #localhost:8000/item/(商品编号)
    path('list/',views.item_list, name = 'item_list'),
    #localhost：8000/item/list
    path("type/<int:items_type_pk>",views.items_with_type,name = 'items_with_type'),
    path("add/",views.item_add,name='item_add')
]