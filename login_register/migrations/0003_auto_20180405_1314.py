# Generated by Django 2.0.2 on 2018-04-05 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_register', '0002_auto_20180405_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_role',
            name='rolename',
            field=models.CharField(default='访客', max_length=30, verbose_name='名称'),
        ),
    ]
