from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=255, db_index=True, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    name = models.CharField(max_length=255, db_index=True, verbose_name='Название')
    slug = models.CharField(max_length=255, db_index=True, unique=True)
    images = RichTextUploadingField(verbose_name='Изображения', blank=True)
    description = models.CharField(max_length=500, verbose_name='Описание', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость')
    stock = models.PositiveIntegerField(verbose_name='Остаток')
    available = models.BooleanField(default=True, verbose_name='Наличие')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['id', 'slug'])]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
