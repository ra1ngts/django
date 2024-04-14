from django.contrib import messages
from django.core.mail import BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .forms import FeedbackForm
from .models import Gallery, About, Category
from .services.email import message_from_feedback
from .services.utils import DataMixin


class Index(DataMixin, ListView):
    model = Gallery
    template_name = 'main/index.html'
    context_object_name = 'gallery'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        addition_context = self.get_user_context(title='Галерея')
        return dict(list(context.items()) + list(addition_context.items()))

    def get_queryset(self):
        return Gallery.objects.filter(is_published=True)


class ShowGallery(DataMixin, ListView):
    model = Gallery
    template_name = 'main/category.html'
    context_object_name = 'gallery'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        addition_context = self.get_user_context(title=f'Галерея: {context["gallery"][0].category}',
                                                 selected=context['gallery'][0].category_id)
        return dict(list(context.items()) + list(addition_context.items()))

    def get_queryset(self):
        return Gallery.objects.filter(category__id=self.kwargs['category_id'], is_published=True)


class Information(DataMixin, ListView):
    model = About
    template_name = 'main/about.html'
    context_object_name = 'information'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(*kwargs)
        addition_context = self.get_user_context(title='О себе')
        return dict(list(context.items()) + list(addition_context.items()))


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
                messages.success(request, 'Ваше сообщение успешно отправлено.')
            except BadHeaderError:
                messages.error(request, 'Неверные данные в форме')
                messages.error(request, form.errors)
    else:
        return HttpResponse('Неверный запрос.')

    data = {'title': 'Контакты',
            'address': 'Россия, г.Москва',
            'phone': '8(123)456-78-90',
            'email': 'example@mail.com',
            'categories': Category.objects.all(),
            'form': form
            }
    return render(request, 'main/contacts.html', context=data)
