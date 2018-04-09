# coding:utf-8
from django.shortcuts import render_to_response, render
from django.http import JsonResponse
from OurCMDB.views import valid_phone,getmd5
from User.forms import AddUser
from User.models import CMDBUser
from PIL import Image

def login(request):
    return render_to_response('login.html')

def index(request):
    adduser = AddUser()
    return render(request, 'index.html', locals())

# ajax提交，电话号码验证函数
def phone_valid(request):
    res = {'type': 'error', 'data': ''}
    if request.method == 'GET':
        phone = request.GET['phone']
        result = valid_phone(phone)
        if phone == result:
            res['type'] = 'success'
        else:
            res['data'] = result
    else:
        res['data'] = 'request must be GET'
    return JsonResponse(res)
def adduser(request):
    res = {'type': 'error', 'data': ''}
    if request.method == 'POST':
        add = AddUser(request.POST, request.FILES)  # 对数据进行校验
        if add.is_valid():
            cleand_data = add.cleaned_data   # 验证通过以后的字典形式的数据
            username = cleand_data['username']
            password = cleand_data['password']
            email = cleand_data['email']
            phone = cleand_data['phone']
            photo = cleand_data['photo']

            user = CMDBUser()
            user.username = username
            user.password = getmd5(password)    # 密码加密
            user.emial = email
            user.phone = phone

            # 创建路径,保存图片
            name = 'static/image/' + photo.name
            img = Image.open(photo)
            img.save(name)
            # 数据库当中存储图片的路径
            user.photo = 'image/' + photo.name
            user.save()

            res['type'] = 'success'
            res['data'] = 'success'

        else:
            res['data'] = add.errors
    else:
        res['data'] = 'request error'
    return JsonResponse(res)
# Create your views here.
