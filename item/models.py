from django.db import models
from django.contrib.auth.models import  User
# Create your models here.


class ItemType(models.Model):
    type_name = models.CharField(max_length = 20)

    def __str__(self):
        return self.type_name


# 定义商品类型
class Item(models.Model):

    # 商品名称
    title = models.CharField (max_length = 30)
    # 商品内容
    content = models.TextField()
    #商品类型
    item_type = models.ForeignKey (ItemType,on_delete= models.DO_NOTHING)
    # 商品主人
    author  = models.ForeignKey (User,on_delete=models.DO_NOTHING)
    # 发布商品的时间
    created_time = models.DateTimeField (auto_now_add= True)
    #最后更新时间
    last_updated_time = models.DateTimeField (auto_now= True)
    # 商品价格 初始为0
    price = models.FloatField(default = 0)


    def  __str__(self):
        return '<Item: %s>'%self.title