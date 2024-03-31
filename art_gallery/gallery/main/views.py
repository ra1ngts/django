from django.shortcuts import render

menu = [{'title': 'Home', 'url_name': 'home'},
        {'title': 'Gallery', 'url_name': 'gallery'},
        {'title': 'About', 'url_name': 'about'},
        {'title': 'Contacts', 'url_name': 'contacts'},
        ]


def index(request):
    data = {'title': 'Home page',
            'menu': menu, }
    return render(request, 'main/index.html', data)


def show_image(request):
    return render(request, 'Show image')


def category(request):
    return render(request, 'Gallery')


def about(request):
    return render(request, 'About')


def contacts(request):
    return render(request, 'Contacts')
