import re
import requests
from django import forms
from django.shortcuts import render, redirect
from login_register import models
# Create your views here.
def index(request):
    
    if request.method == 'POST':
        user = Login_User(request.POST)
        if user.is_valid():
            username = user.cleaned_data['username']
            password = user.cleaned_data['password']

            try:
                readuser = models.Person.objects.get(username=username)

                if readuser.password == password:
                    '''
                        关闭浏览器进程session无效
                        session在60分钟后无效
                    '''
                    request.session['login'] = username

                    # return redirect('http://http://127.0.0.1:8000/login_register/inside')
                    return render(request, 'login_register/try_inside.html',{'username':username,'write':"ok"})
                else:
                    user = Login_User()
                    return render(request, 'login_register/self_login.html', {'user': user,
                                                                         'alert': 'alert',
                                                                         'write': '密码错误'})
            except:
                user = Login_User()
                return render(request, 'login_register/self_login.html', {'user': user,
                                                                     'alert': 'alert',
                                                                     'write': '用户名不存在'})
        else:
            user = Login_User()

            return render(request, 'login_register/self_login.html', {'user': user,
                                                                 'alert': 'alert',
                                                                 'write': '输入有误或用户名不存在'})
    else:
        user = Login_User()
        return render(request, 'ALG_web/home.html', {'user': user})

class User(forms.ModelForm):
    """创建表单"""
    class Meta:
        model = models.Person
        fields = [
            'username',
            'password',
            'name',
            'telephone',
            'age',
            'grade',
        ]
        widgets = {
            'password': forms.PasswordInput(),
        }
        labels = {
            'grade': '年级',
        }

# 新建一个登陆用户的类用来做登陆的表单验证

class Login_User(forms.ModelForm):
    class Meta:
        model = models.Person
        fields = [
            'username',
            'password',
        ]
        widgets = {
            'password' : forms.PasswordInput(),
        }
