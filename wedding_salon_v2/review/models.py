from django.db import models


class Review(models.Model):
    name = models.CharField(max_length=32, verbose_name='Имя')
    review = models.TextField(blank=True, verbose_name='Отзыв')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    is_published = models.BooleanField(default=False, verbose_name='Публикация')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-time_create']
