from django.db import models

# Create your models here.
from django.contrib.auth.models import  User


class ItemType(models.Model):
    type_name = models.CharField(max_length = 20)

    def __str__(self):
        return self.type_name


class Item(models.Model):
    title = models.CharField (max_length = 30)
    content = models.TextField()
    item_type = models.ForeignKey (ItemType,on_delete= models.DO_NOTHING)
    author  = models.ForeignKey (User,on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField (auto_now_add= True)
    last_updated_time = models.DateTimeField (auto_now= True)
    price = models.FloatField(default = 0)

    def  __str__(self):
        return '<Item: %s>'%self.title