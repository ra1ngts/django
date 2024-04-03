from django.db import models


class Gallery(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='paintings/%Y/%m/%d', default=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
