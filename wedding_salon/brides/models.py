from django.db import models
from django.urls import reverse


class Bride(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    main_photo = models.ImageField(upload_to='photos/brides/main/%Y/%m/%d', default=True,
                                   verbose_name='Главная фотография')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    bcat = models.ForeignKey('BrideCategory', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('look_bride', kwargs={'bride_slug': self.slug})

    class Meta:
        verbose_name = 'Невеста'
        verbose_name_plural = 'Невесты'
        ordering = ['title']


class BrideCategory(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('brides_category', kwargs={'cat_brides_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id', 'name']


class BrideImage(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    photo = models.ImageField(upload_to='photos/brides/%Y/%m/%d', verbose_name='Фотография')
    bride_photo = models.ForeignKey(Bride, on_delete=models.CASCADE, related_name='photos',
                                    verbose_name='Синхронизация')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ['id', 'title']
