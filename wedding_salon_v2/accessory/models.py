from django.db import models
from django.urls import reverse

from services.resources import COLORS, AVAILABILITY


class Color(models.Model):
    color = models.CharField(max_length=21, choices=COLORS, verbose_name='Цвет')

    def __str__(self):
        return self.color

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'


class Accessory(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    color = models.ManyToManyField(Color, verbose_name='Цвет')
    price = models.DecimalField(default=0, max_digits=7, decimal_places=2, verbose_name='Стоимость')
    availability = models.CharField(max_length=13, choices=AVAILABILITY, verbose_name='Наличие')
    main_photo = models.ImageField(upload_to='photos/accessories/main/%Y/%m/%d', default=True,
                                   verbose_name='Главная фотография')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    acat = models.ForeignKey('AccessoryCategory', on_delete=models.PROTECT, null=True, verbose_name='Категория')
    rating = models.IntegerField(default=0, verbose_name='Рейтинг')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('look_accessory', kwargs={'accessory_slug': self.slug})

    class Meta:
        verbose_name = 'Аксессуар'
        verbose_name_plural = 'Аксессуары'
        ordering = ['title', 'price']


class AccessoryCategory(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('accessories_category', kwargs={'acat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id', 'title']


class AccessoryImage(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    photo = models.ImageField(upload_to='photos/accessories/%Y/%m/%d', verbose_name='Фотография')
    accessory_photo = models.ForeignKey(Accessory, on_delete=models.CASCADE, related_name='photos',
                                        verbose_name='Синхронизация')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ['id', 'title']
