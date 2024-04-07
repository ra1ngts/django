from django.contrib import admin

from .models import Gallery, Category


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image', 'is_published', 'cat']
    list_display_links = ['title', 'image', 'cat']
    list_editable = ['is_published']
    list_filter = ['title', 'is_published', 'cat']
    search_fields = ['title', 'is_published', 'cat']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['title']
