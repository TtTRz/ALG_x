import re
import requests
from django import forms
from django.shortcuts import render, redirect
from login_register import models
# Create your views here.
def index(request):
    return render(request, 'ALG_web/home.html')

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
