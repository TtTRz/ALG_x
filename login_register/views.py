import re

import requests
from django import forms
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render, redirect

from . import models
from .decorate import login_test
from .email_test import send_email_test


# Create your views here.


class User(forms.ModelForm):
    """创建表单"""

    class Meta:
        model = models.Person
        fields = [
            'username',
            'password',
            'email',
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
            'password': forms.PasswordInput(),
        }


class Find_Password(forms.ModelForm):
    class Meta:
        model = models.Person
        fields = [
            'username',
            'email',
        ]


def es_test(username, password):
    """教务登陆验证"""
    try:

        # 获取表单信息
        url = 'http://es.bnuz.edu.cn/default2.aspx'
        header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

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


def es_login(request):
    """教务账户登陆"""
    if request.method == 'POST':
        user = Login_User(request.POST)

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

                # if not models.Person.objects.get(username = username):
                #     models.Person.objects.create(username=username, password=password)
                try:
                    models.Person.objects.get(username=username)
                except models.Person.DoesNotExist:
                    p = models.Person()
                    p.username = username
                    p.password = password
                    p.save()

                """
                    直接使用get函数
                    当找不到匹配的query时
                    会报DoesNotExit exception
                    错误例子：
                    if not models.Person.objects.get(username = username):
                        models.Person.objects.create(username=username, password=password)
                """

                # return redirect('http://http://127.0.0.1:8000/login_register/inside')
                return redirect("/")

            else:
                user = Login_User()
                return render(request, 'login_register/es_login.html', {'user': user,
                                                                        'alert': 'alert',
                                                                        'write': '密码错误'})
        else:
            user = Login_User()
            return render(request, 'login_register/es_login.html', {'user': user,
                                                                    'alert': 'alert',
                                                                    'write': '输入有误或用户名不存在'})
    else:
        user = Login_User()
        return render(request, 'login_register/es_login.html', {'user': user})


def self_login(request):
    """数据库账户登陆"""
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
                    return redirect("/")
                else:
                    user = Login_User()
                    return render(request, 'ALG_web/home.html', {'user': user,
                                                                              'alert': 'alert',
                                                                              'write': '密码错误'})
            except:
                user = Login_User()
                return render(request, 'ALG_web/home.html', {'user': user,
                                                                          'alert': 'alert',
                                                                          'write': '用户名不存在'})
        else:
            user = Login_User()

            return render(request, 'ALG_web/home.html', {'user': user,
                                                                      'alert': 'alert',
                                                                      'write': '输入有误或用户名不存在'})
    else:
        user = Login_User()
        return render(request, 'ALG_web/home.html', {'user': user})


def create(request):
    """注册账户"""
    if request.method == 'POST':
        user = User(request.POST)

        if user.is_valid():
            username = user.cleaned_data['username']
            email = user.cleaned_data['email']
            try:
                models.Person.objects.get(username=username)
                user = User()
                return render(request, 'ALG_web/home.html', {'user': user,
                                                                           'alert': 'alert',
                                                                           'write': '用户名已存在'})
            except models.Person.DoesNotExist:
                try:
                    models.Person.objects.get(email=email)
                    user = User()
                    return render(request, 'ALG_web/home.html', {'user': user,
                                                                               'alert': 'alert',
                                                                               'write': '邮箱已注册!'})
                except models.Person.DoesNotExist:
                    role = models.User_Role.objects.get(rolename='访客')
                    username = user.cleaned_data['username']
                    user.save()
                    new_user = models.Person.objects.get(username=username)
                    new_user.role = role
                    new_user.save()

                    send_email_test(email, 'create_user')
                    return render(request, 'login_register/Prompt.html')

    else:
        user = User()
        return render(request, 'ALG_web/home.html', {'user': user})


# def inside(request):
#     """内部视图（测试）"""
#     if request.session.get('login'):
#         return render(request, 'login_register/try_inside.html')
#     else:
#         user = Login_User()
#         return render(request, 'login_register/self_login.html', {'user': user,
#                                                                   'alert': 'alert',
                                                                  # 'write': '宝贝先登陆 cnm'})


def log_off(request):
    """取消登陆"""
    request.session['login'] = None
    return redirect('/')


# def find_password(request):
#     """找回密码"""
#     if request.method == 'POST':
#         user = Find_Password(request.POST)
#         if user.is_valid():
#             email = user.cleaned_data['email']
#             username = user.cleaned_data['username']
#             send_email_test(email, 'find_password')


def action_user(request, random_str):
    """激活账户"""
    try:
        user = models.Person.objects.get(code=random_str)
        role = models.User_Role.objects.get(rolename='用户')
        user.role = role
        user.save()

        # rs_type用作激活成功与否标志
        return render(request, 'login_register/email_test.html', {'rs_type' : 1})
    except:
        return render(request, 'login_register/email_test.html', {'rs_type' : 0})




@login_test
def person_information(request):
    """用户个人中心"""
    if request.method == 'POST':
        user = User(request.POST)
        if user.is_valid():
            models.Person.objects.get(username=request.session['login']).delete()
            user.save()
            person = models.Person.objects.get(username=request.session['login'])
            rolename = models.User_Role.objects.get(rolename="用户")
            person.role = rolename
            person.save()
            person = models.Person.objects.get(username=request.session['login'])
            user = User(initial=model_to_dict(person))
            return render(request, 'login_register/user_information.html', {'user': user,
                                                                            'alert' : 'alert',
                                                                            'write' : '修改成功。'})
    else:
        person = models.Person.objects.get(username=request.session['login'])
        user = User(initial=model_to_dict(person))
        return render(request, 'login_register/user_information.html', {'user': user})