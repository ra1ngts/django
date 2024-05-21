from django.db import models
from django.urls import reverse


class Gallery(models.Model):
    class STATUS(models.IntegerChoices):
        PUBLISHED = 1, 'Опубликовано'
        NOT_PUBLISHED = 0, 'Не опубликовано'

    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, verbose_name='Изображение')
    published = models.BooleanField(default=STATUS.PUBLISHED,
                                    choices=tuple(map(lambda x: (bool(x[0]), x[1]), STATUS.choices)),
                                    verbose_name='Публикация')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'
        ordering = ['title']


class Category(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_gallery', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class About(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    content = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='images/about', blank=True, verbose_name='Фотография')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Обо мне'
        verbose_name_plural = 'Обо мне'
