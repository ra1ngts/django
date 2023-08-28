from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Product, Category


def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {'products': products,
               'categories': categories,
               'title': 'Главная страница',
               'cat_selected': 0,
               }
    return render(request, 'shop/index.html', context=context)


def product_category(request, category_slug):
    products = Product.objects.filter(category__slug=category_slug)
    categories = Category.objects.all()
    if len(products) == 0:
        raise Http404()
    context = {'products': products,
               'categories': categories,
               'title': 'Главная страница',
               'cat_selected': category_slug,
               }
    return render(request, 'shop/index.html', context=context)


def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)

    context = {
        'product': product,
        'title': f'Товар: {product.title}',
        'cat_selected': 1,
    }

    return render(request, 'shop/detail.html', context=context)


def about(request):
    return render(request, 'shop/about.html', {'title': 'О сайте'})
