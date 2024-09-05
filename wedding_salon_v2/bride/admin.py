from django.contrib import admin

from .models import Bride, BrideCategory, BrideImage


@admin.register(Bride)
class BrideAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'main_photo', 'is_published', 'bcat']
    list_display_links = ['id', 'is_published']
    search_fields = ['id', 'title', 'is_published']
    list_editable = ['title', 'main_photo']
    list_filter = ['title', 'is_published']
    prepopulated_fields = {'slug': ['title']}


@admin.register(BrideCategory)
class BrideCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title']
    prepopulated_fields = {'slug': ['title']}


@admin.register(BrideImage)
class BrideImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'photo', 'bride_photo']
    list_display_links = ['id', 'bride_photo']
    search_fields = ['id', 'title', 'bride_photo']
    list_editable = ['title', 'photo']
    list_filter = ['title', 'bride_photo']
