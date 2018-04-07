import re

import requests
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect

from . import models


# Create your views here.


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


def es_test(username, password):
    """教务登陆验证"""
    try:

        # 获取表单信息
        url = 'http://es.bnuz.edu.cn/default2.aspx'
        header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

        r = requests.get(url, headers=header)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        html = r.text
        data = {
            "__EVENTTARGET": '',
            "__EVENTARGUMENT": '',
            "__VIEWSTATE": eval(re.findall('".*?"', re.findall('id="__VIEWSTATE" value=".*?" />', html)[0])[1]),
            "__VIEWSTATEGENERATOR": eval(
                re.findall('".*?"', re.findall('id="__VIEWSTATEGENERATOR" value=".*?" />', html)[0])[1]),
            "__PREVIOUSPAGE": eval(re.findall('".*?"', re.findall('id="__PREVIOUSPAGE" value=".*?" />', html)[0])[1]),
            "__EVENTVALIDATION": eval(
                re.findall('".*?"', re.findall('id="__EVENTVALIDATION" value=".*?" />', html)[0])[1]),
            "TextBox1": username,
            "TextBox2": password,
            "RadioButtonList1": "学生",
            "Button4_test": ''
        }

        # 登陆验证
        s = requests.post(url, data=data, headers=header)
        s.raise_for_status()
        s.encoding = s.apparent_encoding
        html2 = s.text

        return True if (username in re.findall('欢迎您：.*?</li>', html2)[0]) else False

    except:
        return False


def login(request, choose):
    """教务账户登陆或者数据库账户登陆"""
    if choose == '1':
        # 教务登陆
        user = User(request.POST)

        if user.is_valid():
            username = user.cleaned_data['username']
            password = user.cleaned_data['password']

            if es_test(username, password):
                """
                    关闭浏览器进程session无效
                    session在60分钟后无效
                """
                request.session['login'] = username

                """若第一次以教务账号登陆，数据库生成该账户信息"""

                if not models.Person.objects.get(username=username):
                    models.Person.objects.create(username=username, password=password)

                return redirect('http://http://127.0.0.1:8000/login_register/inside')
            else:
                user = User()
                return render(request, 'login_register/login.html', {'user': user,
                                                                     'alert': 'alert',
                                                                     'write': '密码错误'})

    elif choose == '2':
        # 数据库账户登陆
        user = User(request.POST)
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

                    return redirect('http://http://127.0.0.1:8000/login_register/inside')
                else:
                    user = User()
                    return render(request, 'login_register/login.html', {'user': user,
                                                                         'alert': 'alert',
                                                                         'write': '密码错误'})
            except:
                user = User()
                return render(request, 'login_register/login.html', {'user': user,
                                                                     'alert': 'alert',
                                                                     'write': '用户名不存在'})
    else:
        user = User()
        return render(request, 'login_register/login.html', {'user': user})


def create(request):
    """注册账户"""
    if request.method == 'POST':
        user = User(request.POST)

        if user.is_valid():
            user.save()
            user = User()

            return render(request, 'login_register/create_user.html', {'user': user})

    else:
        user = User()
        return render(request, 'login_register/create_user.html', {'user': user})


def inside(request):
    """内部视图（测试）"""
    if request.session['login']:
        return render(request, 'login_register/try_inside.html')
    else:
        return HttpResponse("gun")
