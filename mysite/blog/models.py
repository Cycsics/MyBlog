#coding=utf-8
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name

class Category(models.Model):
    """
    博客分类
    """
    name=models.CharField('名称',max_length=30)

    class Meta:
        verbose_name = "类别"
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField('名称',max_length=16)

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name

# Create your models here.
class BlogsPost(models.Model):
    title = models.CharField(max_length = 150)                 # 博客标题
    simple = models.TextField(max_length = 50)                 # 博客正文简略
    body = models.TextField()                                  # 博客正文
    timestamp = models.DateTimeField()                         # 创建时间
    
    class Meta:
        verbose_name = "博客"
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name

class Comment(models.Model):
    blog = models.ForeignKey(BlogsPost,verbose_name='博客',on_delete = models.CASCADE)#(博客--评论:一对多)
    name = models.CharField('称呼',max_length = 16)
    email = models.EmailField('邮箱')
    content = models.CharField('内容',max_length = 240)
    pub = models.DateField('发布时间',auto_now_add = True)

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = "评论"
    def __unicode__(self):
        return self.content
