# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CMDBUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('username', models.CharField(verbose_name='用户名', max_length=32)),
                ('password', models.CharField(verbose_name='密码', max_length=32)),
                ('email', models.EmailField(verbose_name='邮箱', max_length=254)),
                ('phone', models.CharField(verbose_name='电话', max_length=32)),
                ('photo', models.ImageField(verbose_name='照片', upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='组名称', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='权限名称', max_length=32)),
                ('obj_id', models.IntegerField(verbose_name='操作对象')),
                ('description', models.TextField(verbose_name='权限描述')),
            ],
        ),
        migrations.CreateModel(
            name='Permission_group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('permission_id', models.IntegerField(verbose_name='权限id')),
                ('group_id', models.IntegerField(verbose_name='组id')),
            ],
        ),
        migrations.CreateModel(
            name='User_group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('user_id', models.IntegerField(verbose_name='用户id')),
                ('group_id', models.IntegerField(verbose_name='组名称')),
            ],
        ),
        migrations.CreateModel(
            name='User_permission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('user_id', models.IntegerField(verbose_name='用户id')),
                ('permission_id', models.IntegerField(verbose_name='权限id')),
            ],
        ),
    ]
