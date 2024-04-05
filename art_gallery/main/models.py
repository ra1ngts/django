from django.db import models
from django.urls import reverse


class Gallery(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/%Y/%m/%d', default=True)
    # slug = models.SlugField(max_length=255, unique=True, db_index=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_image', kwargs={'post_id': self.pk})


class Category(models.Model):
    title = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_category', kwargs={'cat_id': self.pk})
