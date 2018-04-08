from django.urls import path
from . import views

# start with blog
urlpatterns = [
    # http://localhost:8000/blog/
    path('', views.item_list, name='item_list'),
    path('<int:blog_pk>', views.blog_detail, name="item_detail"),
    path('type/<int:blog_type_pk>', views.items_with_type, name="items_with_type"),
    path('date/<int:year>/<int:month>', views.items_with_date, name="items_with_date"),
]