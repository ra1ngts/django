from allauth.account.views import (SignupView, LoginView, LogoutView,
                                   PasswordChangeView, PasswordResetView, PasswordResetFromKeyView)
from django.contrib import messages
from django.urls import reverse_lazy

from django.views.generic import TemplateView

from services.utils import DataMixin
from .forms import PasswordResetKeyForm


class UsersSignupView(DataMixin, SignupView):
    template_name = 'account/signup.html'
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title='Регистрация')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(self.request, messages.SUCCESS, 'Вы успешно зарегистрировались в системе.',
                             extra_tags='signup')
        return response


class UsersLoginView(DataMixin, LoginView):
    template_name = 'account/login.html'
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title='Войти')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(self.request, messages.SUCCESS, 'Вы успешно вошли в систему.', extra_tags='login')
        return response


class UsersLogoutView(DataMixin, LogoutView):
    template_name = 'account/logout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title='Выйти')


class PasswordsChangeView(DataMixin, PasswordChangeView):
    template_name = 'account/change_password.html'
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title='Изменить пароль')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(self.request, messages.SUCCESS, 'Вы успешно изменили пароль.',
                             extra_tags='change_password')
        return response


class PasswordsResetView(DataMixin, PasswordResetView):
    template_name = 'account/reset_password.html'
    success_url = reverse_lazy('reset_done_password')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title='Сброс пароля')


class PasswordsResetFromKeyView(DataMixin, PasswordResetFromKeyView):
    template_name = 'account/reset_key_password.html'
    form_class = PasswordResetKeyForm
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title='Новый пароль')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(self.request, messages.SUCCESS, 'Вы успешно установили новый пароль.',
                             extra_tags='reset_password_done')
        return response


class PasswordsResetDoneView(DataMixin, TemplateView):
    template_name = 'account/reset_done_password.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        messages.add_message(self.request, messages.SUCCESS,
                             'Мы отправили вам письмо. Если вы его не получили, проверьте папку "Спам".',
                             extra_tags='reset_done')
        return self.get_mixin_context(context, title='Успешный сброс пароля')


class UsersProfileView(DataMixin, TemplateView):
    template_name = 'account/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title='Профиль')
