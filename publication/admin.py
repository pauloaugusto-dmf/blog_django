from django.contrib import admin

from.models import Topic, Post

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'modified']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'topic', 'author', 'created', 'modified']