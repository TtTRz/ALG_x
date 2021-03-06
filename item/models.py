from django.db import models
from django.contrib.auth.models import  User
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.fields import GenericRelation
from read_statistics.models import ReadNumExpandMethod, ReadDetail

from login_register.models import Person
# Create your models here.

#商品第一种标签
class ItemType(models.Model,ReadNumExpandMethod):
    type_name = models.CharField(max_length = 20)

    def __str__(self):
        return self.type_name

# # 定义商品状态
# class ItemState(models.Model,ReadNumExpandMethod):
#     # 状态名称
#     state_name = models.CharField('状态', max_length=30)
#     # 状态等级
#     permission = models.IntegerField('状态等级', default=1)
#
#     def __str__(self):
#
#         return self.state_name
#
#     '''
#         状态：
#             public：
#                 允许所有操作-------1
#             private：
#                 不允许展示不允许交易------2
#             locked：
#                 不允许展示取消订单后后允许交易-------3
#
#     '''


# 定义商品类型
class Item(models.Model,ReadNumExpandMethod):
    # 商品名称
    title = models.CharField (max_length = 10)
    # 商品内容,富文本编辑，可上传文件
    content =RichTextUploadingField(blank = True)
    #商品类型
    item_type = models.ForeignKey (ItemType,on_delete= models.DO_NOTHING,blank =True)
    # 商品状态初始为public
    # item_state = models.ForeignKey (ItemState,on_delete=models.DO_NOTHING)
    # 商品主人
    author  = models.ForeignKey (Person,on_delete=models.DO_NOTHING)
    # 发布商品的时间
    created_time = models.DateTimeField (auto_now_add= True)
    #最后更新时间
    last_updated_time = models.DateTimeField (auto_now= True)
    # 商品价格 初始为0
    price = models.FloatField(default = 0,blank =True)
    pic = models.ImageField(upload_to = 'img',null=False,blank=True,verbose_name='上传图片')
    read_details = GenericRelation(ReadDetail)



    def  __str__(self):
        return '<Item: %s>'%self.title
    #按照发布时间的倒序排列
    class Meta:
        ordering = ['-created_time']

#detail页面显示商品内容的地方参数后面加|safe，显示图片否则会变成代码展现