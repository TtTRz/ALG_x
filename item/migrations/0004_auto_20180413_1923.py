# Generated by Django 2.0.4 on 2018-04-13 11:23

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_auto_20180413_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
