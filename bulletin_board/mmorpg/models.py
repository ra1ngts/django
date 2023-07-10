from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Категория')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('post_category', args=[str(self.pk)])


class Post(models.Model):
    author_post = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    title_post = models.CharField(max_length=255, verbose_name='Заголовок')
    text_post = RichTextUploadingField(verbose_name='Контент')
    category_post = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    date_post = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return f'объявлению: "{self.title_post}" в категории "{self.category_post}" от {self.author_post}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])


class Comment(models.Model):
    author_comment = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    text_comment = models.TextField(verbose_name='Текст')
    post_comment = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Комментарий')
    date_comment = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    confirmation_comment = models.BooleanField(default=False, verbose_name='Подтверждение')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.author_comment} {self.text_comment} {self.post_comment}'

    def get_absolute_url(self):
        return reverse('comment_detail', args=[str(self.pk)])
