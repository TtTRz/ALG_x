from django.urls import path
from .import views

app_name = 'login_register'

urlpatterns = [
    path('create/', views.create, name='create'),
    path('inside/', views.inside, name='inside'),
    path('login/<str:choose>', views.login, name='login'),
    path('inside/', views.inside),
]
