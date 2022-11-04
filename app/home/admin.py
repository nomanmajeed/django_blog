from django.contrib import admin
from .models import Blog, Profile

# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "slug", "user")
    search_fields = ("user","title")
    
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "is_verified")
    search_fields = ("user",)