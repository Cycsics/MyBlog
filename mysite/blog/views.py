from django.shortcuts import render, render_to_response, get_object_or_404
from blog.models import BlogsPost,User
from django import forms
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import auth
from django.views.generic.base import View
from django.http import JsonResponse
import time 
from .models import BlogsPost
from blog import models
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

 
def ajax_list(request):
    a = list(range(100))
    return JsonResponse(a, safe=False)

class UserForm(forms.Form):
    username = forms.CharField(label = '用户名：',max_length=100)
    password = forms.CharField(label = '密码：',widget = forms.PasswordInput())

# class blogIndex(View):
#     """用户登录"""
#     def get(self,request):
#         blog_list = BlogsPost.objects.all()
#         return render(request,'index.html', {'blog_list':blog_list})
#     def post(self,request):
#         uf = UserForm(request.POST)
#         print(uf)
#         if uf.is_valid():
#             #获取表单用户密码
#             username = uf.cleaned_data['username']
#             password = uf.cleaned_data['password']
#             print("username:{0}\tpassword:{0}\n".format(username,password))
#             user=authenticate(username=username,password=password)
#             if user is not None:
#                 login(request,user)
#                 return render_to_response('success.html',{'username':username})
#             else:
#                 return HttpResponse('{"status":"fail"},{"msg":"用户名或密码错误"}')
#         else:
#             uf = UserForm()

def blogAdd(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request,'blogAdd.html')   # 返回index.html页面
        elif request.method == 'POST':
            blogInfo = {}
            blogInfo['Title'] = request.POST['title']
            blogInfo['content'] = request.POST['content']
            blogInfo['Time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(blogInfo)
            blogCreate = models.BlogsPost(
                title = blogInfo['Title'],
                Author = request.user.username,
                simple = blogInfo['content'][:50],
                body = blogInfo['content'],
                timestamp = blogInfo['Time']
            )
            blogCreate.save()
            msg = "成功上传博客"
            return render(request,'report.html',{'msg':msg,'status':'success','urlname':'blogAdd'})
    else:
        msg = "请先登录，才能发表博客"
        return render(request,'report.html',{'msg':msg,'status':'failed'})

def blogIndex(request):
    if request.method == 'GET':
        blog_list = BlogsPost.objects.all()  # 获取所有数据
        return render(request,'index.html', {'blog_list':blog_list})   # 返回index.html页面
    if request.method == 'POST':
        userdata = {}
        userdata['username'] = request.POST['username']
        userdata['password'] = request.POST['Password']
        
        user = authenticate(username = userdata['username'],password = userdata['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                msg = "用户{0}成功登陆".format(userdata['username'])
                return render(request, "report.html", {'msg':msg,'status':'success'})
        else:
            msg = "用户名或密码错误，请重新登陆"
            return render(request,"report.html",{'msg':msg,'status':'failed'})
        # uf = UserForm(request.POST)
        # if uf.is_valid():
        #     #获取表单用户密码
        #     username = uf.cleaned_data['username']
        #     password = uf.cleaned_data['password']
        #     #获取的表单数据与数据库进行比较
        #     user = User.objects.filter(username__exact = username,password__exact = password)
        #     if user:
        #         return render_to_response('success.html',{'username':username})
        #     else:
        #         return HttpResponseRedirect('/login/')



def register(request):
    if request.method == 'GET':
        return render(request,'register.html',{})
    elif request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            msg = "请输入一样的密码"
            return render(request,'register.html',{'msg':msg})
        else:
            userPost = User.objects.create_user(
                username=username,
                password=password1
            )
            # userPost = models.User(
            #     username = username,
            #     password = password1
            # )
            userPost.save()
            msg = "成功注册用户,用户名为：{0}".format(username)
            return render(request,'report.html',{'msg':msg,'urlname':'register'})

def blogChange(request,uid):
    if request.method == 'GET':
        bloginfo = BlogsPost.objects.get(id = uid)
        return render(request, 'blogChange.html', {'blogInfo': bloginfo})
    elif request.method == 'POST':
        blogInfo = {}
        blogInfo['Title'] = request.POST['title']
        blogInfo['content'] = request.POST['content']
        blog = BlogsPost.objects.get(id = uid)
        blog.body = blogInfo['content']
        blog.save()
        msg = "成功修改博客"
        return render(request,'report.html',{'msg':msg})

def log_out(request):
    logout(request)
    return render(request,'index.html',{})

def blogInfo(request,uid):
    if request.method == 'GET':
        bloginfo = BlogsPost.objects.get(id = uid)
        # print(uid)
        return render(request,'blogInfo.html',{'blogInfo':bloginfo})
    else:
        pass