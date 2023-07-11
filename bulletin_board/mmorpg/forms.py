from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from mmorpg.models import Post, Category, Comment


class PostForm(forms.ModelForm):
    title_post = forms.CharField(label='Заголовок')
    text_post = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент')
    category_post = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Не выбрана')

    class Meta:
        model = Post
        fields = ['title_post', 'text_post', 'category_post']


class CommentForm(forms.ModelForm):
    text_comment = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}), label='Текст')

    class Meta:
        model = Comment
        fields = ['text_comment']
