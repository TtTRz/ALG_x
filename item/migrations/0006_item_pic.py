# Generated by Django 2.0.2 on 2018-05-09 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_auto_20180418_0743'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='pic',
            field=models.ImageField(blank=True, upload_to='img', verbose_name='上传图片'),
        ),
    ]
