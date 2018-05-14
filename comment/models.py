from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import  ContentType
from login_register.models import Person
# Create your models here.
class Comment(models.Model):
    content_type = models.ForeignKey(ContentType,on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type','object_id')

    text = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Person,on_delete=models.DO_NOTHING)