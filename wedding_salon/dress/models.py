from django.db import models
from django.urls import reverse

from dress.resources import COLORS, DIMENSIONS, TEXTILE, AVAILABILITY


class Size(models.Model):
    size = models.CharField(max_length=12, choices=DIMENSIONS, verbose_name='Размер')

    def __str__(self):
        return self.size

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'


class Textile(models.Model):
    textile = models.CharField(max_length=10, choices=TEXTILE, verbose_name='Ткань')

    def __str__(self):
        return self.textile

    class Meta:
        verbose_name = 'Ткань'
        verbose_name_plural = 'Ткани'


class Color(models.Model):
    color = models.CharField(max_length=15, choices=COLORS, verbose_name='Цвет')

    def __str__(self):
        return self.color

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'


class Dress(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    color = models.ManyToManyField(Color, verbose_name='Цвет')
    textile = models.ManyToManyField(Textile, verbose_name='Ткань')
    size = models.ManyToManyField(Size, verbose_name='Размер')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена')
    availability = models.CharField(max_length=13, choices=AVAILABILITY, verbose_name='Наличие')
    main_photo = models.ImageField(upload_to='photos/dresses/main/%Y/%m/%d', default=True,
                                   verbose_name='Главная фотография')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    cat = models.ForeignKey('DressCategory', on_delete=models.PROTECT, verbose_name='Категория')
    rating = models.IntegerField(default=0, verbose_name='Рейтинг')

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('look_dress', kwargs={'dress_slug': self.slug})

    class Meta:
        verbose_name = 'Свадебное платье'
        verbose_name_plural = 'Свадебные платья'
        ordering = ['title', 'price']


class DressCategory(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dresses_category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id', 'name']


class DressImage(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    photo = models.ImageField(upload_to='photos/dresses/%Y/%m/%d', verbose_name='Фотография')
    dress_photo = models.ForeignKey(Dress, on_delete=models.CASCADE, related_name='photos',
                                    verbose_name='Синхронизация')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ['id', 'title']
