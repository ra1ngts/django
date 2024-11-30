# Generated by Django 5.0.6 on 2024-11-30 16:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrideCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['id', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Bride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('main_photo', models.ImageField(default=True, upload_to='photos/brides/main/%Y/%m/%d', verbose_name='Главная фотография')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
                ('bcat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bride.bridecategory', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Невеста',
                'verbose_name_plural': 'Невесты',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='BrideImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('photo', models.ImageField(upload_to='photos/brides/%Y/%m/%d', verbose_name='Фотография')),
                ('bride_photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='bride.bride', verbose_name='Синхронизация')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
                'ordering': ['id', 'title'],
            },
        ),
    ]
