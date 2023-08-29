from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Post)
class AdminPost(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'body']
    list_display_links = ['author']
