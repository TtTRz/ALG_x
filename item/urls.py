from django.urls import path

from .import views
urlpatterns = [

    path('<int:item_pk>',views.item_detail,name = 'item_detail'),
    path('list/',views.item_list,name = 'item_list'),
]