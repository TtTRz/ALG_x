# Generated by Django 2.0.3 on 2018-04-09 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_register', '0006_auto_20180405_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='person',
            name='grade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login_register.User_Grade'),
        ),
        migrations.AlterField(
            model_name='person',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login_register.User_Role'),
        ),
        migrations.AlterField(
            model_name='person',
            name='username',
            field=models.CharField(default='', max_length=30, verbose_name='用户名'),
        ),
    ]
