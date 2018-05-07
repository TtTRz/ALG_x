from django.db import models

# Create your models here.

class User_Role(models.Model):
    # 角色名称
    rolename = models.CharField('名称', max_length = 30, default='')
    # 角色权限等级
    permission = models.IntegerField('权限等级', default=3)

    def __str__(self):
        return self.rolename

    '''
        角色权限：
            管理员:
                允许拥有所有权限 ----------- 1
            用  户:
                允许进行买卖交易, 上传商品 -- 2
            访  客:
                允许进行商品浏览   --------- 3
    '''

class User_Grade(models.Model):
    # 年级名称
    gradename = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.gradename



class Person(models.Model):
    # 用户名
    username = models.CharField('用户名', max_length=30, default='')
    # 用户密码
    password = models.CharField('密码', max_length=30, default='')
    # 用户年龄
    age = models.IntegerField('年龄', default=0, null=True,blank=True)
    # 用户角色
    role = models.ForeignKey('User_Role', on_delete=models.CASCADE, null=True, blank=True)
    # 用户所处年级
    grade = models.ForeignKey('User_Grade', on_delete=models.CASCADE, null=True, blank=True)
    # 用户真实名称
    name = models.CharField('真实姓名', max_length=30, default='', null=True)
    # 联系电话
    telephone = models.CharField('联系电话', max_length = 20, default='', null=True)
    # 邮箱地址
    email = models.EmailField('邮箱地址', max_length=50, default='')
    # 邮箱随机密文
    code = models.CharField(max_length=50, default='', null=True, blank=True)




    def __str__(self):
        return self.username

