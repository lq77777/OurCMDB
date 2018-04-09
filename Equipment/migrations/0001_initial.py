# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('hostname', models.CharField(verbose_name='主机名', max_length=32)),
                ('mac', models.CharField(verbose_name='mac地址', max_length=32)),
                ('ip', models.CharField(verbose_name='ip地址', max_length=32)),
                ('sys_type', models.CharField(verbose_name='系统类型', max_length=32)),
                ('sys_version', models.CharField(verbose_name='系统版本', max_length=32)),
                ('cpu_count', models.CharField(verbose_name='cpu使用率', max_length=32)),
                ('disk', models.CharField(verbose_name='硬盘', max_length=32)),
                ('memory', models.CharField(verbose_name='内存', max_length=32)),
            ],
        ),
    ]
