from django.contrib import admin

from salon.models import Salon, Services, Master, User


class SalonAdmin(admin.ModelAdmin):
    list_display = ('title', 'info', 'time', 'address', 'phone', 'email', 'web')
    list_display_links = ('title', 'info', 'time', 'address', 'phone', 'email', 'web')
    list_filter = ('title', 'info', 'time', 'address', 'phone', 'email', 'web')


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'services', 'price')
    list_display_links = ('title', 'text', 'services', 'price')
    list_filter = ('title', 'price', 'services')


class MasterAdmin(admin.ModelAdmin):
    list_display = ('name', 'avatar', 'info', 'portfolio')
    list_display_links = ('name', 'avatar', 'info', 'portfolio')
    list_filter = ('name', 'avatar', 'info', 'portfolio')


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'date', 'salon', 'services', 'master')
    list_display_links = ('name', 'phone', 'email', 'date', 'salon', 'services', 'master')
    list_filter = ('name', 'phone', 'email', 'date', 'salon', 'services', 'master')


admin.site.register(Salon, SalonAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Master, MasterAdmin)
admin.site.register(User, UserAdmin)
