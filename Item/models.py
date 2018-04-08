from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
# from ckeditor_uploader.fields import RichTextUploadingField
from read_statistics.models import ReadNumExpandMethod, ReadDetail

class ItemType(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name

class Item(models.Model, ReadNumExpandMethod):
    title = models.CharField(max_length=50)
    item_type = models.ForeignKey(ItemType, on_delete=models.DO_NOTHING)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    read_details = GenericRelation(ReadDetail)
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "<Item: %s>" % self.title

    class Meta:
        ordering = ['-created_time']
