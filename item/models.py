from django.db import models
from django.contrib.auth.models import  User
from ckeditor_uploader.fields import RichTextUploadingField
<<<<<<< HEAD
=======
from django.contrib.contenttypes.fields import GenericRelation
from read_statistics.models import ReadNumExpandMethod, ReadDetail
>>>>>>> ea29281fada114167064b81158c2ce87b5b3eafb
# Create your models here.

#商品第一种标签
class ItemType(models.Model,ReadNumExpandMethod):
    type_name = models.CharField(max_length = 20)

    def __str__(self):
        return self.type_name


# 定义商品类型
class Item(models.Model,ReadNumExpandMethod):
    # 商品名称
<<<<<<< HEAD
    title = models.CharField (max_length = 30)
    # 商品内容,富文本编辑，可上传文件
    content =RichTextUploadingField()
=======
    title = models.CharField (max_length = 10)
    # 商品内容,富文本编辑，可上传文件
    content =RichTextUploadingField(blank = True)
>>>>>>> ea29281fada114167064b81158c2ce87b5b3eafb
    #商品类型
    item_type = models.ForeignKey (ItemType,on_delete= models.DO_NOTHING,blank =True)
    # 商品主人
    author  = models.ForeignKey (User,on_delete=models.DO_NOTHING)
    # 发布商品的时间
    created_time = models.DateTimeField (auto_now_add= True)
    #最后更新时间
    last_updated_time = models.DateTimeField (auto_now= True)
    # 商品价格 初始为0
    price = models.FloatField(default = 0,blank =True)
    read_details = GenericRelation(ReadDetail)



    def  __str__(self):
        return '<Item: %s>'%self.title
    #按照发布时间的倒序排列
    class Meta:
        ordering = ['-created_time']

#detail页面显示商品内容的地方参数后面加|safe，显示图片否则会变成代码展现