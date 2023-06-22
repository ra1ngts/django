from django.contrib import admin

from review.models import Review, CategoryReview


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'review', 'time_create', 'is_published')
    list_display_links = ('name', 'review')
    search_fields = ('name',)
    list_editable = ('is_published',)
    list_filter = ('name', 'is_published')


class CategoryReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Review, ReviewAdmin)
admin.site.register(CategoryReview, CategoryReviewAdmin)
