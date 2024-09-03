from captcha.fields import CaptchaField
from django import forms
from django.utils.translation import gettext_lazy as _


class FeedbackForm(forms.Form):
    first_name = forms.CharField(max_length=150, label=_('Имя'))
    last_name = forms.CharField(max_length=150, label=_('Фамилия'), required=False)
    email = forms.EmailField(label=_('Электронная почта'))
    subject = forms.CharField(max_length=255, label=_('Заголовок'))
    message = forms.CharField(widget=forms.Textarea(attrs={'cols': 30, 'row': 7}), label=_('Сообщение'))
    captcha = CaptchaField(label=_('Проверка'))

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            first_name_plcholder = _('Имя')
            last_name_plcholder = _('Фамилия')
            email_plcholder = _('Электронная почта')
            subject_plcholder = _('Заголовок')
            message_plcholder = _('Введите свое сообщение или вопрос...')
            captcha_plcholder = _('Проверочный код с изображения')
            if name == 'first_name':
                field.widget.attrs.update({'placeholder': first_name_plcholder})
            if name == 'last_name':
                field.widget.attrs.update({'placeholder': last_name_plcholder})
            if name == 'email':
                field.widget.attrs.update({'placeholder': email_plcholder})
            if name == 'subject':
                field.widget.attrs.update({'placeholder': subject_plcholder})
            if name == 'message':
                field.widget.attrs.update({'placeholder': message_plcholder})
            if name == 'captcha':
                field.widget.attrs.update({'placeholder': captcha_plcholder})
            field.widget.attrs.update({'class': 'form-control'})
