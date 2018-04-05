from django import forms
from django.shortcuts import render

from . import models


# Create your views here.

class User(forms.ModelForm):
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


def create(request):
    if request.method == 'POST':
        user = User(request.POST)

        if user.is_valid():
            user.save()
            user = User()

            return render(request, 'login_register/create_user.html', {'user': user})

    else:
        user = User()
        return render(request, 'login_register/create_user.html', {'user': user})
