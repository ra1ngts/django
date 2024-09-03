from django.contrib import admin

from shop.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'title', 'slug', 'image', 'description', 'price', 'available', 'created',
                    'updated']
    list_filter = ['category', 'title', 'price', 'available', 'created', 'updated']
    list_editable = ['category', 'title', 'price']
    prepopulated_fields = {'slug': ('title',)}
