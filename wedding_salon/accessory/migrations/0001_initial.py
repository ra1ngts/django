# Generated by Django 4.2 on 2023-05-19 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена')),
                ('availability', models.CharField(choices=[('В наличии', 'В наличии'), ('Нет в наличии', 'Нет в наличии')], max_length=13, verbose_name='Наличие')),
                ('main_photo', models.ImageField(default=True, upload_to='photos/accessories/main/%Y/%m/%d', verbose_name='Главная фотография')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
            ],
            options={
                'verbose_name': 'Аксессуар',
                'verbose_name_plural': 'Аксессуары',
                'ordering': ['title', 'price'],
            },
        ),
        migrations.CreateModel(
            name='AccessoryCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['id', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(choices=[('Белый', 'Белый'), ('Молочный', 'Молочный'), ('Кремовый', 'Кремовый'), ('Айвори', 'Айвори'), ('Розовый', 'Розовый'), ('Красный', 'Красный'), ('Мятный', 'Мятный'), ('Синий', 'Синий'), ('Черный', 'Черный')], max_length=15, verbose_name='Цвет')),
            ],
            options={
                'verbose_name': 'Цвет',
                'verbose_name_plural': 'Цвета',
            },
        ),
        migrations.CreateModel(
            name='AccessoryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('photo', models.ImageField(upload_to='photos/accessories/%Y/%m/%d', verbose_name='Фотография')),
                ('accessory_photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='accessory.accessory', verbose_name='Синхронизация')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
                'ordering': ['id', 'title'],
            },
        ),
        migrations.AddField(
            model_name='accessory',
            name='acat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='accessory.accessorycategory', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='accessory',
            name='color',
            field=models.ManyToManyField(to='accessory.color', verbose_name='Цвет'),
        ),
    ]
