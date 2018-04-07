from django.urls import path
from .import views

app_name = 'login_register'

urlpatterns = [
    path('create/', views.create, name='create'),
    path('inside/', views.inside, name='inside'),
    path('self_login/', views.self_login, name='self_login'),
    path('es_login/', views.es_login, name='es_login'),
    path('inside/', views.inside),
]
