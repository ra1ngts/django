from django import forms
from django.core.exceptions import ValidationError

from news.models import Post, Author


class NewsForm(forms.ModelForm):
    author_post = forms.ModelChoiceField(queryset=Author.objects.all(), label='Автор', empty_label='Не выбран')
    title_post = forms.CharField(label='Заголовок')
    text_post = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 10}), label='Текст')

    class Meta:
        model = Post
        fields = ['author_post', 'title_post', 'text_post', 'categories_post']
        labels = {'categories_post': 'Категория'}

    def clean(self):
        cleaned_data = super().clean()
        title_post = cleaned_data.get('title_post')
        text_post = cleaned_data.get('text_post')

        if title_post == text_post:
            raise ValidationError('Текст "новости / статьи" не должен быть идентичен заголовку')

        return cleaned_data
