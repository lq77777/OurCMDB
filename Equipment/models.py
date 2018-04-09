#coding:utf-8
from django.db import models

# 设备表
class Equipment(models.Model):
    hostname = models.CharField(max_length=32, verbose_name='主机名')
    mac = models.CharField(max_length=32, verbose_name='mac地址')
    ip = models.CharField(max_length=32, verbose_name='ip地址')
    sys_type = models.CharField(max_length=32, verbose_name='系统类型')
    sys_version = models.CharField(max_length=32, verbose_name='系统版本')
    cpu_count = models.CharField(max_length=32, verbose_name='cpu使用率')
    disk = models.CharField(max_length=32,verbose_name='硬盘')
    memory = models.CharField(max_length=32, verbose_name='内存')

    def __unicode__(self):
        # unicode返回对象
        return "%s:%s" % (self.hostname, self.ip)  # 用于后台展示
# Create your models here.
