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
            body = blogInfo['content'],
            timestamp = blogInfo['Time']
        )
        blogCreate.save()
        msg = "成功上传博客"
        return render(request,'success.html',{'msg':msg})

def blogIndex(request):
    if request.method == 'GET':
        blog_list = BlogsPost.objects.all()  # 获取所有数据
        return render(request,'index.html', {'blog_list':blog_list})   # 返回index.html页面
    if request.method == 'POST':
        userdata = {}
        userdata['username'] = request.POST['username']
        userdata['pws'] = request.POST['password']
        msg = "用户{0}成功登陆".format(userdata['username'])
        user = User.objects.filter(username__exact = username,password__exact = password)
        return render(request, "success.html", msg)
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
    else:
        uf = UserForm()
    return render(request,'index.html', {'blog_list':blog_list})   # 返回index.html页面


#登录
def login(request):
    blog_list = BlogsPost.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('Password')
        user = User.objects.filter(username__exact = username,password__exact = password)
        if user:
            return render_to_response('index.html',{'username':username,'blog_list':blog_list})
    else:
        return render_to_response('index.html',{'username':username,'blog_list':blog_list})
    return render_to_response('index.html',{'blog_list':blog_list})

def view_post(request, slug):
    return render_to_response('blogpost_detail.html', {
        'post': get_object_or_404(BlogPost, slug=slug)
    })



def addBlog(request):
    if request.is_ajax():
        username = request.POST.get('username')
        password = request.POST.get('Password')
        data = {}
        data['status'] = '0'
        data['message'] = '传递数据成功'
        data['data'] = {'title':title,'content':content}
        return JsonResponse(data)
    else:
        username = request.POST.get('username')
        username = request.POST.get('Password')
        print(title)
        print(content)
        return render(request, 'index.html', locals())
