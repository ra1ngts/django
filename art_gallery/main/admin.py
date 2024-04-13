from django.contrib import admin

from .models import Gallery, Category, About


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image', 'is_published', 'category']
    list_display_links = ['title', 'image', 'category']
    list_editable = ['is_published']
    list_filter = ['title', 'is_published', 'category']
    search_fields = ['title', 'is_published', 'category']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['title']


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'photo']
    list_display_links = ['title', 'photo']
