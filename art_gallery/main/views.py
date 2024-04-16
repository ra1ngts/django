from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from .forms import FeedbackForm
from .models import Gallery, About
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


class Contacts(SuccessMessageMixin, FormView):
    form_class = FeedbackForm
    template_name = 'main/contacts.html'
    success_url = reverse_lazy('contacts')
    success_message = 'Ваше сообщение успешно отправлено.'
    extra_context = {'title': 'Контакты',
                     'address': 'Россия, г.Москва',
                     'phone': '8(123)456-78-90',
                     'email': 'example@mail.com'
                     }

    def form_valid(self, form):
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        captcha = form.cleaned_data['captcha']
        message_from_feedback(first_name, last_name, email, subject, message, captcha)
        print(f'С контактной формы поступило новое сообщение от {first_name} с электронной почты: {email}')
        return super().form_valid(form)


def trace_handler403(request, exception):
    context = {'title': 'Ошибка доступа: 403',
               'error_message': 'Ошибка доступа: 403'
               }
    return render(request=request, template_name='error.html', status=403, context=context)


def trace_handler404(request, exception):
    context = {'title': 'Страница не найдена: 404',
               'error_message': 'Страница не найдена: 404'
               }
    return render(request=request, template_name='error.html', status=404, context=context)


def trace_handler500(request):
    context = {'title': 'Ошибка сервера: 500',
               'error_message': 'Ошибка сервера: 500'
               }
    return render(request=request, template_name='error.html', status=500, context=context)
