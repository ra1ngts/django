from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from .forms import FeedbackForm
from .models import Gallery, About
from .services.email import message_from_feedback
from .services.utils import DataMixin
from django.utils.translation import gettext_lazy as _


class Index(DataMixin, ListView):
    model = Gallery
    template_name = 'main/index.html'
    context_object_name = 'gallery'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        addition_context = self.get_user_context(title=_('Галерея'))
        return dict(list(context.items()) + list(addition_context.items()))

    def get_queryset(self):
        return Gallery.objects.filter(published=Gallery.STATUS.PUBLISHED).order_by('-title')


class ShowGallery(DataMixin, ListView):
    model = Gallery
    template_name = 'main/category.html'
    context_object_name = 'gallery'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        title = _('Галерея')
        addition_context = self.get_user_context(title=f'{title}: {context["gallery"][0].category}',
                                                 selected=context['gallery'][0].category_id)
        return dict(list(context.items()) + list(addition_context.items()))

    def get_queryset(self):
        return Gallery.objects.filter(category__id=self.kwargs['category_id'], published=Gallery.STATUS.PUBLISHED)


class Information(DataMixin, ListView):
    model = About
    template_name = 'main/about.html'
    context_object_name = 'information'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(*kwargs)
        addition_context = self.get_user_context(title=_('Обо мне'))
        return dict(list(context.items()) + list(addition_context.items()))


class Contacts(SuccessMessageMixin, DataMixin, FormView):
    form_class = FeedbackForm
    template_name = 'main/contacts.html'
    success_url = reverse_lazy('contacts')
    success_message = _('Ваше сообщение успешно отправлено.')
    extra_context = {'title': _('Контакты'),
                     'address_title': _('Адрес'),
                     'address': _('Россия, г.Москва'),
                     'phone_title': _('Телефон'),
                     'phone': '+71234567890',
                     'email_title': _('Электронная почта'),
                     'email': 'example@mail.com',
                     'cv_title': _('Резюме'),
                     'cv_link': '#'
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(**kwargs)
        context.update(user_context)
        return context


def trace_handler403(request, exception):
    context = {'title': _('Ошибка доступа: 403'),
               'error_message': _('Ошибка доступа: 403')
               }
    return render(request=request, template_name='error.html', status=403, context=context)


def trace_handler404(request, exception):
    context = {'title': _('Страница не найдена: 404'),
               'error_message': _('Страница не найдена: 404')
               }
    return render(request=request, template_name='error.html', status=404, context=context)


def trace_handler500(request):
    context = {'title': _('Ошибка сервера: 500'),
               'error_message': _('Ошибка сервера: 500')
               }
    return render(request=request, template_name='error.html', status=500, context=context)
