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
            placeholder = _('Введите свое сообщение или вопрос...')
            if name == 'message':
                field.widget.attrs.update({'placeholder': placeholder})
            field.widget.attrs.update({'class': 'form-control'})
