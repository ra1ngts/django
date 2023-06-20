from django.contrib.auth.models import User
from django.core.cache import cache
from django.db import models
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.urls import reverse

from news.resources import CATEGORY
from django.utils.translation import gettext_lazy as _


class Author(models.Model):
    author_user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('Автор'))
    rating_user = models.IntegerField(default=0, verbose_name=_('Рейтинг'))

    class Meta:
        verbose_name = _('Автор')
        verbose_name_plural = _('Авторы')

    def update_rating(self):
        rating_posts_author = \
            Post.objects.filter(author_post=self).aggregate(rating_post=Coalesce(Sum('rating_post'), 0))[
                'rating_post'] * 3
        rating_comments_author = Comment.objects.filter(user_comment=self.author_user).aggregate(
            rating_comment=Coalesce(Sum('rating_comment'), 0))['rating_comment']
        rating_comments_posts = Comment.objects.filter(post_comment__author_post=self.id).aggregate(
            rating_comment=Coalesce(Sum('rating_comment'), 0))['rating_comment']

        self.rating_user = rating_posts_author + rating_comments_author + rating_comments_posts
        print(self.rating_user)
        self.save()

    def __str__(self):
        return f'{self.author_user}'


class Category(models.Model):
    title_category = models.CharField(max_length=255, unique=True, verbose_name=_('Название новости или статьи'))
    subscribers = models.ManyToManyField(User, related_name='categories')

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')

    def __str__(self):
        return self.title_category


class Post(models.Model):
    title_post = models.CharField(max_length=255, verbose_name=_('Название'))
    text_post = models.TextField(verbose_name=_('Текст'))
    author_post = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name=_('Автор'))
    choice_post = models.CharField(max_length=7, choices=CATEGORY, verbose_name=_('Выбор публикации'))
    date_post = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата'))
    categories_post = models.ManyToManyField(Category, through='PostCategory', verbose_name=_('Категория публикации'))
    rating_post = models.IntegerField(default=0, verbose_name=_('Рейтинг'))

    class Meta:
        verbose_name = _('Публикация')
        verbose_name_plural = _('Публикации')

    def like(self):
        self.rating_post += 1
        self.save()

    def dislike(self):
        self.rating_post -= 1
        self.save()

    def preview(self):
        if len(self.text_post) <= 124:
            return self.text_post
        else:
            return self.text_post[0:124] + '...'

    def __str__(self):
        return f"{self.title_post} {self.text_post} {self.author_post}"

    def get_absolute_url(self):
        return reverse('news', args=[str(self.id)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete(f'show_news: {self.pk}')


class PostCategory(models.Model):
    post_category = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name=_('Публикация'))
    category_post = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('Категория'))

    class Meta:
        verbose_name = _('Категория публикации')
        verbose_name_plural = _('Категории публикаций')

    def __str__(self):
        return f'{self.post_category} {self.category_post}'


class Comment(models.Model):
    post_comment = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name=_('Публикация'))
    user_comment = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Автор'))
    text_comment = models.TextField(default='', verbose_name=_('Текст'))
    date_comment = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата'))
    rating_comment = models.IntegerField(default=0, verbose_name=_('Рейтинг'))

    class Meta:
        verbose_name = _('Комментарий')
        verbose_name_plural = _('Комментарии')

    def like(self):
        self.rating_comment += 1
        self.save()

    def dislike(self):
        self.rating_comment -= 1
        self.save()

    def __str__(self):
        return f'{self.text_comment} {self.rating_comment}'
