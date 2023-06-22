from django.contrib import admin

from dress.models import Dress, DressCategory, DressImage, Color, Textile, Size


class SizeAdmin(admin.ModelAdmin):
    list_display = ('size',)


class TextileAdmin(admin.ModelAdmin):
    list_display = ('textile',)


class ColorAdmin(admin.ModelAdmin):
    list_display = ('color',)


class DressAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'availability', 'main_photo', 'is_published')
    list_display_links = ('id', 'title', 'price', 'availability', 'main_photo')
    search_fields = ('id', 'title', 'color', 'textile', 'size', 'price', 'availability')
    list_editable = ('is_published',)
    list_filter = ('title', 'color', 'price', 'availability')
    prepopulated_fields = {'slug': ('title',)}


class DressCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class DressImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo', 'dress_photo')
    list_display_links = ('id', 'photo', 'dress_photo')
    search_fields = ('id', 'title', 'dress_photo')
    list_editable = ('title',)
    list_filter = ('title', 'dress_photo')


admin.site.register(Size, SizeAdmin)
admin.site.register(Textile, TextileAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Dress, DressAdmin)
admin.site.register(DressCategory, DressCategoryAdmin)
admin.site.register(DressImage, DressImageAdmin)
