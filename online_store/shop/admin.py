from django.contrib import admin

from shop.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']
    list_filter = ['name']
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'name', 'images', 'description', 'price', 'stock', 'available', 'created',
                    'updated']
    list_display_links = ['category', 'name', 'description', 'price', 'stock', 'available']
    list_filter = ['id', 'category', 'name', 'price', 'stock', 'available', 'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
