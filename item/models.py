from django.db import models

# Create your models here.
from django.contrib.auth.models import  User


class ItemType(models.Model):
    type_name = models.CharField(max_length = 20)

    def __str__(self):
        return self.type_name
# 定义商品类型

class Item(models.Model):
    title = models.CharField (max_length = 30)#商品名称
    content = models.TextField()#商品内容
    item_type = models.ForeignKey (ItemType,on_delete= models.DO_NOTHING)
    author  = models.ForeignKey (User,on_delete=models.DO_NOTHING) #商品主人
    created_time = models.DateTimeField (auto_now_add= True)#发布商品的时间
    last_updated_time = models.DateTimeField (auto_now= True)
    price = models.FloatField(default = 0)#商品价格 初始为0

    def  __str__(self):
        return '<Item: %s>'%self.title