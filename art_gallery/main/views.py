from django.core.mail import BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from .forms import FeedbackForm
from .models import Gallery, About
from .services.email import message_from_feedback


class Index(ListView):
    model = Gallery
    template_name = 'main/index.html'
    context_object_name = 'gallery'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Галерея'
        return context

    def get_queryset(self):
        return Gallery.objects.filter(is_published=True)


class ShowGallery(ListView):
    model = Gallery
    template_name = 'main/category.html'
    context_object_name = 'gallery'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Галерея: {context["gallery"][0].category}'
        context['selected'] = context['gallery'][0].category_id
        return context

    def get_queryset(self):
        return Gallery.objects.filter(category__id=self.kwargs['category_id'], is_published=True)


class Information(ListView):
    model = About
    template_name = 'main/about.html'
    context_object_name = 'information'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(*kwargs)
        context['title'] = 'О себе'
        return context


class Contacts(FormView):
    form_class = FeedbackForm
    template_name = 'main/contacts.html'
    success_url = reverse_lazy('success')
    extra_context = {'title': 'Контакты',
                     'address': 'Россия, г.Москва',
                     'phone': '8(123)456-78-90',
                     'email': 'example@mail.com'
                     }

    def form_valid(self, form):
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
        else:
            return HttpResponse('Неверный запрос.')
        return super(Contacts, self).form_valid(form)


def success(request):
    return render(request, 'main/email/success_email_send.html')
