from django.db import models
from django.urls import reverse


class Gallery(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, verbose_name='Изображение')
    # slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_image', kwargs={'img_id': self.pk})

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'
        ordering = ['title']


class Category(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_gallery', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
