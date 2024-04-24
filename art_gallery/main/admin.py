from django.contrib import admin

from .models import Gallery, Category, About


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image', 'published', 'category']
    list_display_links = ['title', 'image', 'category']
    list_editable = ['published']
    list_filter = ['title', 'published', 'category']
    search_fields = ['title', 'published', 'category']
    list_per_page = 10


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['title']


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'photo']
    list_display_links = ['title', 'photo']
