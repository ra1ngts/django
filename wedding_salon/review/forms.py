from django import forms
from django.core.exceptions import ValidationError

from review.models import Review


class AddReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['add_review'].empty_label = 'Не публиковать'

    class Meta:
        model = Review
        fields = ['name', 'review', 'add_review']
        widgets = {'title': forms.TextInput(attrs={'class': 'form-input'}),
                   'review': forms.Textarea(attrs={'cols': 60, 'rows': 10})
                   }

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        review = cleaned_data.get('review')
        if name == review:
            raise ValidationError('Отзыв не должен быть идентичен имени')

        return cleaned_data

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 200:
            raise ValidationError('Длина заголовка превышает 200 символов')

        return name
