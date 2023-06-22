from django.contrib import admin

from accessory.models import Accessory, AccessoryCategory, AccessoryImage, Color


class ColorAdmin(admin.ModelAdmin):
    list_display = ('color',)


class AccessoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'availability', 'main_photo', 'is_published')
    list_display_links = ('id', 'title', 'price', 'availability', 'main_photo')
    search_fields = ('id', 'title', 'color', 'price', 'availability')
    list_editable = ('is_published',)
    list_filter = ('title', 'color', 'price', 'availability', 'is_published')
    prepopulated_fields = {'slug': ('title',)}


class AccessoryCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class AccessoryImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo', 'accessory_photo')
    list_display_links = ('id', 'photo', 'accessory_photo')
    search_fields = ('id', 'title', 'accessory_photo')
    list_editable = ('title',)
    list_filter = ('title', 'accessory_photo')


admin.site.register(Color, ColorAdmin)
admin.site.register(Accessory, AccessoryAdmin)
admin.site.register(AccessoryCategory, AccessoryCategoryAdmin)
admin.site.register(AccessoryImage, AccessoryImageAdmin)
