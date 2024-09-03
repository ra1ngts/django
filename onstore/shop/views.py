from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product, Category


class ProductList(ListView):
    model = Product
    template_name = 'shop/index.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Product.objects.filter(available=True)


class ProductCategory(ListView):
    model = Product
    template_name = 'shop/index.html'
    context_object_name = 'products'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['title'] = f'Категория: {str(context["products"][0].category)}'
        context['cat_selected'] = context["products"][0].category
        return context

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['category_slug'])


class ProductDetail(DetailView):
    model = Product
    template_name = 'shop/detail.html'
    context_object_name = 'product'
    slug_url_kwarg = 'product_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Товар: {context["product"].category} / {context["product"].title}'
        return context


def about(request):
    return render(request, 'shop/about.html', {'title': 'О сайте'})
