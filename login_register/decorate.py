"""
所在视图函数
from login_register.decorate import login_test

在需要验证的视图上添加
@login_test即可
"""

from django.http import HttpResponse

from . import models


def login_test(func):
    def test(request, *args, **kwargs):
        if request.session.get('login'):
            user = models.Person.objects.get(username=request.session['login'])
            if user.role.rolename == "用户":
                return func(request, *args, **kwargs)
            elif user.role.rolename == "访客":
                return HttpResponse("账户未激活")
        else:
            return HttpResponse("登陆")

    return test
