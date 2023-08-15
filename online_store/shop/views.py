from django.views.generic import ListView

from .models import Category, Product


class CategoriesListView(ListView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'category'


class ProductsListView(ListView):
    model = Product
    template_name = 'all_products.html'
    context_object_name = 'products'
