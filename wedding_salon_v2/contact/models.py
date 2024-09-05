from django.db import models


class Contact(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    address = models.TextField(verbose_name='Адрес')
    weekdays = models.CharField(max_length=100, verbose_name='ПН-ПТ')
    weekends = models.CharField(max_length=255, verbose_name='СБ, ВС')
    phone = models.CharField(max_length=49, verbose_name='Телефон')
    email = models.CharField(max_length=60, verbose_name='E-mail')
    instagram = models.CharField(max_length=100, verbose_name='Instagram')
    vk = models.CharField(max_length=100, verbose_name='VK')
    photo_1 = models.ImageField(upload_to="photos/contact/", verbose_name='Фотография 1')
    photo_2 = models.ImageField(upload_to="photos/contact/", verbose_name='Фотография 2')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
