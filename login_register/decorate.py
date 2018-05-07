"""
登陆验证装饰器
"""

from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from .models import Person

from . import models


class User(forms.ModelForm):
    class Meta():
        model = Person
        fields = [
            'username',
            'password',
        ]
        widgets = {
            'password' : forms.PasswordInput(),
        }

def login_test(func):
    def test(request, *args, **kwargs):
        if request.session.get('login'):
            print(request.session.get('login'))
            user = models.Person.objects.get(username=request.session['login'])
            try:
                if user.role.rolename == "用户":
                    return func(request, *args, **kwargs)
            except:
                user = User()
                return render(request, 'login_register/self_login.html', {'user': user,
                                                                          'alert': 'alert',
                                                                          'write': '账户未激活'})

        else:
            user = User()
            return render(request, 'login_register/self_login.html', {'user': user,
                                                                      'alert': 'alert',
                                                                      'write': '请先登陆'})

    return test
