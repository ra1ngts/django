from django.shortcuts import render

from .models import Gallery


def index(request):
    gallery = Gallery.objects.all()
    data = {'title': 'Галерея',
            'gallery': gallery
            }
    return render(request, 'main/index.html', context=data)


def show_gallery(request, cat_id):
    gallery = Gallery.objects.filter(cat_id=cat_id)
    data = {'title': f'Галерея: {cat_id}',
            'gallery': gallery,
            'selected': cat_id
            }
    return render(request, 'main/category.html', context=data)


def about(request):
    data = {'title': 'Обо мне'}
    return render(request, 'main/about.html', context=data)


def contacts(request):
    data = {'title': 'Контакты'}
    return render(request, 'main/contacts.html', context=data)
