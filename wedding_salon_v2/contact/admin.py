from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'address', 'weekdays', 'weekends', 'phone', 'email', 'instagram', 'vk', 'photo_1',
                    'photo_2']
    list_display_links = ['id', 'title', 'address', 'weekdays', 'weekends', 'phone', 'email', 'instagram', 'vk']
