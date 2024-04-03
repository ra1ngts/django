from django.shortcuts import render

menu = [{'title': 'Home', 'url_name': 'home'},
        {'title': 'Gallery', 'url_name': 'gallery'},
        {'title': 'About', 'url_name': 'about'},
        {'title': 'Contacts', 'url_name': 'contacts'},
        ]


def index(request):
    return render(request, 'main/index.html')


def category(request):
    return render(request, 'main/category.html')


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')
