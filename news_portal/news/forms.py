from django import forms
from django.core.exceptions import ValidationError

from news.models import Post, Author
from django.utils.translation import gettext_lazy as _


class NewsForm(forms.ModelForm):
    author_post = forms.ModelChoiceField(queryset=Author.objects.all(), label=_('Автор'), empty_label=_('Не выбран'))
    title_post = forms.CharField(label=_('Заголовок'))
    text_post = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 10}), label=_('Text'))

    class Meta:
        model = Post
        fields = ['author_post', 'title_post', 'text_post', 'categories_post']
        labels = {'categories_post': _('Категория публикации')}


def clean(self):
    cleaned_data = super().clean()
    title_post = cleaned_data.get('title_post')
    text_post = cleaned_data.get('text_post')

    if title_post == text_post:
        raise ValidationError('Текст "новости / статьи" не должен быть идентичен заголовку')

    return cleaned_data
