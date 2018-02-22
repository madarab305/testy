from django.contrib import admin
from django.contrib import admin
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp", "updated"]
    class Meta:
        model = Post

# Register your models here.
