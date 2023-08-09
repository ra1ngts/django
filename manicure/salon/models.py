from django.db import models

from salon.resources import SERVICES


class Salon(models.Model):
    title = models.CharField(max_length=255, blank=True, verbose_name='Название салона')
    info = models.TextField(blank=True, verbose_name='О салоне')
    time = models.CharField(max_length=255, blank=True, help_text='БЕЗ ВЫХОДНЫХ с 10:00 до 22:00',
                            verbose_name='Часы работы')
    address = models.TextField(max_length=255, blank=True, verbose_name='Адрес')
    phone = models.CharField(max_length=12, blank=True, help_text='Формат ввода: +70123456789', verbose_name='Телефон')
    email = models.EmailField(max_length=30, blank=True, verbose_name='Электронная почта')
    web = models.CharField(max_length=255, blank=True, verbose_name='Сайт')

    class Meta:
        verbose_name = 'Салон'
        verbose_name_plural = 'Салоны'

    def __str__(self):
        return f'{self.title}'


class Services(models.Model):
    title = models.CharField(max_length=255, blank=True, verbose_name='Название услуги')
    text = models.TextField(blank=True, verbose_name='Описание услуги')
    services = models.CharField(max_length=9, choices=SERVICES, default='nails', verbose_name='Выбор услуги')
    price = models.FloatField(default=0.0, null=True, verbose_name='Стоимость услуги')
    salon = models.ManyToManyField(Salon, verbose_name='Выбор салона')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return f'{self.title}'


class Master(models.Model):
    name = models.CharField(max_length=50, blank=True, verbose_name='Имя мастера')
    avatar = models.ImageField(blank=True, verbose_name='Фотография мастера')
    info = models.TextField(blank=True, verbose_name='Описание работ мастера')
    portfolio = models.URLField(blank=True, verbose_name='Фотографии работ')
    salon = models.ManyToManyField(Salon, verbose_name='Салон мастера')
    services = models.ManyToManyField(Services, verbose_name='Услуги мастера')

    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'

    def __str__(self):
        return f'{self.name}'


class User(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    phone = models.CharField(max_length=12, help_text='Формат ввода: +70123456789', verbose_name='Телефон')
    email = models.EmailField(max_length=30, verbose_name='Электронная почта')
    date = models.DateTimeField(verbose_name='Дата и время записи')
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE, verbose_name='Выбор салона для записи')
    services = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name='Выбор услуги')
    master = models.ForeignKey(Master, on_delete=models.CASCADE, verbose_name='Выбор мастера')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'{self.name}'
