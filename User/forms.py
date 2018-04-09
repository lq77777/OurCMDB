#coding:utf-8

import re
from django import forms
from django.forms import ValidationError
from User.models import CMDBUser
from OurCMDB.views import valid_phone

class AddUser(forms.Form):
    username = forms.CharField(max_length=32,
                               min_length=6,
                               label='用户名',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '用户名'})
                               )
    password = forms.CharField(max_length=32,
                               min_length=6,
                               label='密码',
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '密码'})
                               )
    email = forms.CharField(max_length=32,
                               min_length=6,
                               label='邮箱',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '邮箱'})
                               )
    phone = forms.CharField(max_length=32,
                               min_length=11,
                               label='电话',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '电话'})
                               )
    photo = forms.ImageField(label='用户头像')

    # 手机号验证
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')  # cleaned_data forms中的方法，获取forms提交的值，数据验证通过后会以字典的形式返回到面向对象的实例中
        result = valid_phone(phone)
        if result == phone:
            return phone
        else:
            raise ValidationError(result)

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password.isdigit():
            raise ValidationError('密码过于简单，请重新设置')
        elif password.isalnum():
            raise ValidationError('密码过于简单，请重新设置')
        else:
            return password
    def clean_email(self):
        email = self.clean_data.get('email')
        res = re.match(r"\w+@\w+\.[a-zA-Z]+", email)
        if res:
            return email
        else:
            raise ValidationError('邮箱格式错误')



