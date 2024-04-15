from captcha.fields import CaptchaField
from django import forms


class FeedbackForm(forms.Form):
    first_name = forms.CharField(max_length=150, label='Имя')
    last_name = forms.CharField(max_length=150, label='Фамилия', required=False)
    email = forms.EmailField(label='Электронная почта')
    subject = forms.CharField(max_length=255, label='Заголовок')
    message = forms.CharField(widget=forms.Textarea(attrs={'cols': 30, 'row': 7}), label='Сообщение')
    captcha = CaptchaField(label='Проверка')

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            placeholder = 'Введите свое сообщение или вопрос...'
            if name == 'message':
                field.widget.attrs.update({'placeholder': placeholder})
            field.widget.attrs.update({'class': 'form-control'})
