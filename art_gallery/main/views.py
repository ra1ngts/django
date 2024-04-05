from django.shortcuts import render

from .models import Category, Gallery


def index(request):
    cats = Category.objects.all()
    data = {'title': 'Home',
            'cats': cats
            }
    return render(request, 'main/index.html', context=data)


def show_category(request, cat_id):
    gallery = Gallery.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    data = {'title': f'Category: {cat_id}',
            'gallery': gallery,
            'cats': cats,
            'cat_selected': cat_id
            }
    return render(request, 'main/category.html', context=data)


def category(request):
    data = {'title': 'Gallery'
            }
    return render(request, 'main/category.html', context=data)


def about(request):
    cats = Category.objects.all()
    data = {'title': 'About',
            'cats': cats
            }
    return render(request, 'main/about.html', context=data)


def contacts(request):
    cats = Category.objects.all()
    data = {'title': 'Contacts',
            'cats': cats
            }
    return render(request, 'main/contacts.html', context=data)


def show_image(request, post_id):
    data = {'title': f'Photo: {post_id}',
            'post_id': post_id
            }
    return render(request, '#', context=data)
