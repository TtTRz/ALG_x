from django.urls import path
from .import views

app_name = 'login_register'

urlpatterns = [
    path('create/', views.create, name='create')
]
