from django.urls import path
from .import views

app_name = 'login_register'

urlpatterns = [
    path('create/', views.create, name='create'),
    path('inside/', views.inside, name='inside'),
    path('self_login/', views.self_login, name='self_login'),
    path('es_login/', views.es_login, name='es_login'),
    path('inside/', views.inside),
    path('log_off/', views.log_off, name='log_off'),
    path('email_test/<str:random_str>', views.action_user, name='email_test'),
    path('user_information/', views.person_information, name='user_information'),
]
