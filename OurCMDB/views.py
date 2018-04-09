# coding:utf-8
from django.shortcuts import render
# from User.forms import AddUser
from User.models import CMDBUser
import hashlib

# base视图
# def base(request):
#     addUser = AddUser()
#     return render(request, 'base.html', locals())

# 校验电话号码
def valid_phone(phone):
    try:
        user = CMDBUser.objects.get(phone=phone)  # 尝试在数据库中查询改手机号
    except:
        return phone  # 假如手机号不存在，返回手机号，改手机号可以注册
    else:
        return '手机号重复'  # 手机号存在，抛出异常，提示手机号重复

# 加密函数
def getmd5(password):
    md5 = hashlib.md5()
    md5.update(password)
    return md5.hexdigest()