from django.contrib import admin

from pereval.models import Pereval, Images, Coords, Users


class UsersAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'patronymic', 'email', 'phone')
    list_display_links = ('first_name', 'last_name', 'patronymic', 'email', 'phone')
    list_filter = ('first_name', 'last_name', 'patronymic', 'email', 'phone')


class PerevalAdmin(admin.ModelAdmin):
    list_display = (
        'beauty_title', 'title', 'other_titles', 'connect', 'add_time', 'status', 'level', 'coordinates', 'user',
        'images')
    list_display_links = ('beauty_title', 'title', 'other_titles', 'connect', 'add_time', 'status', 'level',
                          'coordinates', 'user', 'images')
    list_filter = (
        'beauty_title', 'title', 'other_titles', 'connect', 'add_time', 'status', 'level', 'coordinates', 'user',
        'images')


class ImagesAdmin(admin.ModelAdmin):
    list_display = ('title_1', 'image_1', 'title_2', 'image_2', 'title_3', 'image_3')
    list_display_links = ('title_1', 'image_1', 'title_2', 'image_2', 'title_3', 'image_3')


class CoordsAdmin(admin.ModelAdmin):
    list_display = ('latitude', 'longitude', 'height')
    list_display_links = ('latitude', 'longitude', 'height')
    list_filter = ('latitude', 'longitude', 'height')


admin.site.register(Users, UsersAdmin)
admin.site.register(Pereval, PerevalAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(Coords, CoordsAdmin)
