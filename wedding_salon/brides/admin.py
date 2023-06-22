from django.contrib import admin

from brides.models import Bride, BrideCategory, BrideImage


class BrideAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'main_photo', 'is_published', 'bcat')
    list_display_links = ('id', 'main_photo', 'is_published')
    search_fields = ('id', 'title', 'is_published')
    list_editable = ('title',)
    list_filter = ('title', 'is_published')
    prepopulated_fields = {'slug': ('title',)}


class BrideCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class BrideImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo', 'bride_photo')
    list_display_links = ('id', 'photo', 'bride_photo')
    search_fields = ('id', 'title', 'bride_photo')
    list_editable = ('title',)
    list_filter = ('title', 'bride_photo')


admin.site.register(Bride, BrideAdmin)
admin.site.register(BrideCategory, BrideCategoryAdmin)
admin.site.register(BrideImage, BrideImageAdmin)
