from django.contrib import admin

from review.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'review', 'time_create', 'is_published']
    list_display_links = ['name', 'review']
    search_fields = ['name']
    list_editable = ['is_published']
    list_filter = ['name', 'is_published']
