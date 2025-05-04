from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import User, Post, Comment, Follower

# Customizing the User model admin
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'bio')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    ordering = ('username',)

# Customizing the Post model admin
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'creater', 'date_created', 'content_text', 'comment_count')
    search_fields = ('creater__username', 'content_text')
    list_filter = ('date_created',)
    ordering = ('-date_created',)

# Customizing the Comment model admin
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'commenter', 'comment_content', 'comment_time')
    search_fields = ('post__id', 'commenter__username', 'comment_content')
    list_filter = ('comment_time',)
    ordering = ('-comment_time',)

# Customizing the Follower model admin
@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    search_fields = ('user__username',)
    ordering = ('user',)