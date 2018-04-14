"""ALG_x URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from ALG_web import views as ALG_web_views
from django.conf.urls import include
from item.views import item_list


urlpatterns = [
    path('',ALG_web_views.index),
    path('login_register/', include('login_register.urls', namespace='Login_register')),
    path('admin/', admin.site.urls),
    path('item/', include('item.urls')),
    path('simditor',include('simditor.urls')),
]

urlpatterns+=static(settings.MEDIA_URL ,document_root = settings.MEDIA_ROOT)
#上传的文件的路径


