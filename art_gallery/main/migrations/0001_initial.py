# Generated by Django 5.0.6 on 2024-06-05 15:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('content', models.TextField(verbose_name='Описание')),
                ('content_ru', models.TextField(null=True, verbose_name='Описание')),
                ('content_en', models.TextField(null=True, verbose_name='Описание')),
                ('photo', models.ImageField(blank=True, upload_to='images/about', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'Обо мне',
                'verbose_name_plural': 'Обо мне',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Название')),
                ('title_ru', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Название')),
                ('title_en', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('image', models.ImageField(blank=True, upload_to='images/%Y/%m/%d', verbose_name='Изображение')),
                ('published', models.BooleanField(choices=[(True, 'Опубликовано'), (False, 'Не опубликовано')], default=1, verbose_name='Публикация')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Галерея',
                'verbose_name_plural': 'Галереи',
                'ordering': ['title'],
            },
        ),
    ]
