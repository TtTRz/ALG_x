from django.contrib import admin
from .models import User_Role,User_Grade,Person
# Register your models here.

admin.site.register(User_Grade)
admin.site.register(User_Role)
admin.site.register(Person)
