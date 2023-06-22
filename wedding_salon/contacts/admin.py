from django.contrib import admin

from contacts.models import Contacts


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'address', 'metro', 'weekdays', 'weekend', 'phones', 'email', 'photo_1', 'photo_2')
    list_display_links = ('id', 'title', 'address', 'metro', 'weekdays', 'weekend', 'phones', 'email')


admin.site.register(Contacts, ContactsAdmin)
