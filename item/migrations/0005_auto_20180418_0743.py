# Generated by Django 2.0.2 on 2018-04-17 23:43

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_auto_20180413_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_type',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='item.ItemType'),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(max_length=10),
        ),
    ]
