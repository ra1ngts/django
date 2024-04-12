from django.core.mail import BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import FeedbackForm
from .models import Gallery
from .services.email import message_from_feedback


def index(request):
    gallery = Gallery.objects.all()
    data = {'title': 'Галерея',
            'gallery': gallery
            }
    return render(request, 'main/index.html', context=data)


def show_gallery(request, cat_id):
    gallery = Gallery.objects.filter(cat_id=cat_id)
    data = {'title': 'Галерея',
            'gallery': gallery,
            'selected': cat_id
            }
    return render(request, 'main/category.html', context=data)


def show_image(request, img_id):
    data = {'title': f'Название: {img_id}',
            'img_id': img_id
            }
    return render(request, 'main/category.html', context=data)


def about(request):
    data = {'title': 'О себе'}
    return render(request, 'main/about.html', context=data)


def contacts(request):
    if request.method == 'GET':
        form = FeedbackForm()
    elif request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            print(f'С контактной формы поступило новое сообщение от {first_name} с электронной почты: {email}')
            try:
                message_from_feedback(first_name, last_name, email, subject, message)
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return redirect('success')
    else:
        return HttpResponse('Неверный запрос.')

    data = {'title': 'Контакты',
            'address': 'Россия, г.Москва',
            'phone': '8(123)456-78-90',
            'email': 'example@mail.com',
            'form': form
            }
    return render(request, 'main/contacts.html', context=data)


def success(request):
    return render(request, 'main/email/success_email_send.html')
