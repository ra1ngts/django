from captcha.fields import CaptchaField
from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    name = forms.CharField(max_length=32, min_length=3, label='Имя')
    review = forms.CharField(min_length=32, widget=forms.Textarea(attrs={'class': 'form-control'}), label='Отзыв')
    captcha = CaptchaField(label='Проверка')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            for_name = 'Имя'
            for_review = 'Отзыв'
            for_captcha = 'Проверочный код с изображения'
            if name == 'name':
                field.widget.attrs.update({'placeholder': for_name})
            if name == 'review':
                field.widget.attrs.update({'placeholder': for_review})
            if name == 'captcha':
                field.widget.attrs.update({'placeholder': for_captcha})
            field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Review
        fields = ['name', 'review', 'captcha']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'review': forms.Textarea(attrs={'class': 'form-control'}),
                   'captcha': forms.Textarea(attrs={'class': 'form-control'}),
                   }
