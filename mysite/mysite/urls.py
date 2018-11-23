"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
# from django.conf.urls import url
from django.contrib import admin
from django.urls import path,re_path
from django.views.generic import TemplateView
from . import search,search2
from blog.views import blogIndex
from blog import views
# from views import blogIndex
# from .views import blog_index


urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^$', TemplateView.as_view(template_name="index.html")),
    # url(r'^$', blogIndex.as_view(),name="index"),
    path('index' , blogIndex,name = 'index'),
    path('search-form', search.search_form),
    path('search', search.search),
    path('search-post', search2.search_post),
    path('ajax_list/', views.ajax_list, name='ajax-list'),
    path('login',views.blogIndex,name = 'login'),
    path('blogAdd',views.blogAdd,name='blogAdd'),
    path('register',views.register,name = 'register'),
    path('logout',views.log_out,name = 'logout'),
    path('blog/<uid>',views.blogInfo,name = 'blogInfo'),
    # url(r'^login/',views.login),
]

if settings.DEBUG:
   from django.contrib.staticfiles import views
   urlpatterns += [
       path('^static/(?P<path>.*)', views.serve),
   ]
