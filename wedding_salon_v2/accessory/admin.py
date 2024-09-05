from django.contrib import admin

from .models import Color, Accessory, AccessoryCategory, AccessoryImage


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['color']


@admin.register(Accessory)
class AccessoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'availability', 'main_photo', 'is_published', 'acat', 'rating']
    list_display_links = ['id', 'title', 'price', 'availability']
    search_fields = ['id', 'title', 'color', 'price', 'availability']
    list_editable = ['main_photo', 'is_published']
    list_filter = ['title', 'color', 'price', 'availability', 'is_published']
    prepopulated_fields = {'slug': ['title']}


@admin.register(AccessoryCategory)
class AccessoryCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title']
    prepopulated_fields = {'slug': ['title']}


@admin.register(AccessoryImage)
class AccessoryImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'photo', 'accessory_photo']
    list_display_links = ['id', 'accessory_photo']
    search_fields = ['id', 'title', 'accessory_photo']
    list_editable = ['title', 'photo']
    list_filter = ['title', 'accessory_photo']
