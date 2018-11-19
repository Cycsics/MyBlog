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
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from . import search,search2
from blog.views import blogIndex
from blog import views
# from views import blogIndex
# from .views import blog_index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', TemplateView.as_view(template_name="index.html")),
    # url(r'^$', blogIndex.as_view(),name="index"),
    url(r'^$' , blogIndex,name = 'index'),
    url(r'^search-form$', search.search_form),
    url(r'^search$', search.search),
    url(r'^search-post$', search2.search_post),
    url(r'^ajax_list/$', views.ajax_list, name='ajax-list'),
    url(r'^login$',views.login,name = 'login'),
    url(r'^blogAdd$',views.blogAdd,name='blogAdd')
    # url(r'^login/',views.login),
]

if settings.DEBUG:
   from django.contrib.staticfiles import views
   urlpatterns += [
       url(r'^static/(?P<path>.*)$', views.serve),
   ]
