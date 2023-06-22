from django.db import models


class Contacts(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    address = models.TextField(blank=True, verbose_name='Адрес')
    metro = models.CharField(max_length=255, verbose_name='Метро')
    weekdays = models.CharField(max_length=255, verbose_name='График работы: ПН-ПТ')
    weekend = models.CharField(max_length=255, verbose_name='График работы: СБ, ВС')
    phones = models.CharField(max_length=255, verbose_name='Телефоны')
    email = models.EmailField(max_length=255, verbose_name='E-mail')
    photo_1 = models.ImageField(upload_to="photos/contacts/", verbose_name='Фотография 1')
    photo_2 = models.ImageField(upload_to="photos/contacts/", verbose_name='Фотография 2')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
