from django.contrib import admin
from .models import *
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','password')

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

class BlogsPostAdmin(admin.ModelAdmin):
    list_display = ('title','simple','body','timestamp')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('blog','name','content','pub')

admin.site.register(User,UserAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(BlogsPost,BlogsPostAdmin)
admin.site.register(Comment,CommentAdmin)
