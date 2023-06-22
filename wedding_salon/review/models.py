from django.db import models


class Review(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    review = models.TextField(blank=True, verbose_name='Отзыв')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    add_review = models.ForeignKey('CategoryReview', on_delete=models.PROTECT, verbose_name='Опубликовать')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-time_create']


class CategoryReview(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id', '-name']
