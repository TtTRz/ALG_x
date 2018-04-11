from django.contrib import admin
from .models import User_Role,User_Grade,Person
# Register your models here.

@admin.register(Person)
class Person(admin.ModelAdmin):
    list_display = ('username', 'role', 'grade', 'name', 'telephone')

@admin.register(User_Grade)
class UserGrade(admin.ModelAdmin):
    list_display = ('gradename',)

@admin.register(User_Role)
class UserRole(admin.ModelAdmin):
    list_display = ('rolename', 'permission')