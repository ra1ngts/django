from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator


class Product(models.Model):
    title = models.CharField(max_length=150, validators=[MinLengthValidator(3)], verbose_name='Название')
    description = models.TextField(validators=[MinLengthValidator(10)], verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], verbose_name='Цена')

    def __str__(self):
        return self.title
