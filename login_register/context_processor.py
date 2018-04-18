from .models import Person
from django import forms

class Login_User(forms.ModelForm):
    class Meta():
        model = Person
        fields = [
            'username',
            'password',
        ]
        widgets = {
            'password' : forms.PasswordInput(),
        }

class Create_User(forms.ModelForm):
    """创建表单"""

    class Meta:
        model = Person
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


def login_forms(request):
    user = Login_User()
    return {'login_user' : user}

def create_forms(request):
    user = Create_User()
    return {'create_user' : user}