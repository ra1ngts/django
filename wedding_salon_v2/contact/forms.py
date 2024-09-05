from captcha.fields import CaptchaField
from django import forms


class FeedBackForm(forms.Form):
    name = forms.CharField(max_length=32, min_length=3, label='Имя')
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(min_length=32, widget=forms.Textarea(attrs={'class': 'form-control'}), label='Сообщение')
    captcha = CaptchaField(label='Проверка')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            for_name = 'Имя'
            for_email = 'Адрес электронной почты'
            for_message = 'Сообщение'
            for_captcha = 'Проверочный код с изображения'
            if name == 'name':
                field.widget.attrs.update({'placeholder': for_name})
            if name == 'email':
                field.widget.attrs.update({'placeholder': for_email})
            if name == 'message':
                field.widget.attrs.update({'placeholder': for_message})
            if name == 'captcha':
                field.widget.attrs.update({'placeholder': for_captcha})
            field.widget.attrs.update({'class': 'form-control'})
