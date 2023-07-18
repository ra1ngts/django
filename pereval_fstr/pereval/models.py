from django.db import models

from pereval.resources import STATUS, LEVEL
from pereval.utils import get_image_path


class Users(models.Model):
    first_name = models.CharField(max_length=15, verbose_name='Имя')
    last_name = models.CharField(max_length=20, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=20, verbose_name='Отчество')
    email = models.EmailField(max_length=30, verbose_name='Электронная почта')
    phone = models.CharField(max_length=12, help_text='Формат ввода: +70123456789', verbose_name='Телефон')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic} {self.email} {self.phone}'


class Pereval(models.Model):
    beauty_title = models.CharField(max_length=255, blank=True, verbose_name='Префикс')
    title = models.CharField(max_length=255, blank=True, verbose_name='Название')
    other_titles = models.CharField(max_length=255, blank=True, verbose_name='Другое название')
    connect = models.CharField(max_length=255, blank=True, verbose_name='Соединяет')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    status = models.CharField(choices=STATUS, max_length=8, default='new', verbose_name='Статус данных')
    level = models.CharField(choices=LEVEL, max_length=9, verbose_name='Категория трудности')
    coordinates = models.ForeignKey('Coords', on_delete=models.CASCADE, verbose_name='Координаты')
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='Пользователь')
    images = models.ForeignKey('Images', on_delete=models.CASCADE, verbose_name='Изображения')

    class Meta:
        verbose_name = 'Перевал'
        verbose_name_plural = 'Перевалы'

    def __str__(self):
        return f'{self.beauty_title} {self.title} {self.other_titles} {self.connect} {self.add_time} {self.status}' \
               f'{self.level} {self.coordinates} {self.user} {self.images}'


class Images(models.Model):
    title_1 = models.CharField(max_length=255, blank=True, verbose_name='Название фото 1')
    image_1 = models.ImageField(max_length=255, upload_to=get_image_path, blank=True, verbose_name='Фотография 1')
    title_2 = models.CharField(max_length=255, blank=True, verbose_name='Название фото 2')
    image_2 = models.ImageField(max_length=255, upload_to=get_image_path, blank=True, verbose_name='Фотография 2')
    title_3 = models.CharField(max_length=255, blank=True, verbose_name='Название фото 3')
    image_3 = models.ImageField(max_length=255, upload_to=get_image_path, blank=True, verbose_name='Фотография 3')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return f'{self.title_1} {self.title_2} {self.title_3}'


class Coords(models.Model):
    latitude = models.FloatField(null=True, verbose_name='Широта')
    longitude = models.FloatField(null=True, verbose_name='Долгота')
    height = models.IntegerField(null=True, verbose_name='Высота')

    class Meta:
        verbose_name = 'Координата'
        verbose_name_plural = 'Координаты'

    def __str__(self):
        return f'{self.latitude} {self.longitude} {self.height}'
