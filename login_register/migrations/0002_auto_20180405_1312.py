# Generated by Django 2.0.2 on 2018-04-05 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gradename', models.CharField(default='大学一年级', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User_Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rolename', models.CharField(default='', max_length=30, verbose_name='名称')),
                ('permission', models.IntegerField(default=3, verbose_name='权限等级')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='password',
            field=models.CharField(default='', max_length=30, verbose_name='密码'),
        ),
        migrations.AddField(
            model_name='person',
            name='telephone',
            field=models.CharField(default='', max_length=20, verbose_name='联系电话'),
        ),
        migrations.AddField(
            model_name='person',
            name='username',
            field=models.CharField(default='', max_length=30, verbose_name='昵称'),
        ),
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(default=0, verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(default='', max_length=30, verbose_name='真实姓名'),
        ),
        migrations.AddField(
            model_name='person',
            name='grade',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='login_register.User_Grade'),
        ),
        migrations.AddField(
            model_name='person',
            name='role',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='login_register.User_Role'),
        ),
    ]
