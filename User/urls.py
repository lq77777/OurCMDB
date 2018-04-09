# coding: utf-8
from django.conf.urls import url
from User.views import *

# 子路由
urlpatterns = [
    url(r'^phone_valid/$', phone_valid),
    url(r'^adduser/$', adduser)

]