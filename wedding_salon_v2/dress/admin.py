from django.contrib import admin

from .models import Color, Size, Textile, Dress, DressCategory, DressImage


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['color']


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['size']


@admin.register(Textile)
class TextileAdmin(admin.ModelAdmin):
    list_display = ['textile']


@admin.register(Dress)
class DressAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'price', 'availability', 'main_photo', 'is_published', 'cat', 'rating']
    list_display_links = ['id', 'title', 'price', 'availability']
    search_fields = ['id', 'title', 'color', 'textile', 'size', 'price', 'availability']
    list_editable = ['main_photo', 'is_published']
    list_filter = ['title', 'color', 'price', 'availability']
    prepopulated_fields = {'slug': ['title']}


@admin.register(DressCategory)
class DressCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ('id', 'title')
    search_fields = ['title']
    prepopulated_fields = {'slug': ['title']}


@admin.register(DressImage)
class DressImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'photo', 'dress_photo']
    list_display_links = ['id', 'dress_photo']
    search_fields = ['id', 'title', 'dress_photo']
    list_editable = ['title', 'photo']
    list_filter = ['title', 'dress_photo']
