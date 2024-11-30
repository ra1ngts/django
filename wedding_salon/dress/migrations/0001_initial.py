# Generated by Django 4.1.7 on 2024-11-30 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
            name='Dress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена')),
                ('availability', models.CharField(choices=[('В наличии', 'В наличии'), ('Нет в наличии', 'Нет в наличии')], max_length=13, verbose_name='Наличие')),
                ('main_photo', models.ImageField(default=True, upload_to='photos/dresses/main/%Y/%m/%d', verbose_name='Главная фотография')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
                ('rating', models.IntegerField(default=0, verbose_name='Рейтинг')),
            ],
            options={
                'verbose_name': 'Свадебное платье',
                'verbose_name_plural': 'Свадебные платья',
                'ordering': ['title', 'price'],
            },
        ),
        migrations.CreateModel(
            name='DressCategory',
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
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('40 - 42 (XS)', '40 - 42 (XS)'), ('42 - 44 (S)', '42 - 44 (S)'), ('44 - 46 (M)', '44 - 46 (M)'), ('46 - 48 (L)', '46 - 48 (L)'), ('48 - 50 (XL)', '48 - 50 (XL)')], max_length=12, verbose_name='Размер')),
            ],
            options={
                'verbose_name': 'Размер',
                'verbose_name_plural': 'Размеры',
            },
        ),
        migrations.CreateModel(
            name='Textile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('textile', models.CharField(choices=[('Гипюр', 'Гипюр'), ('Фатин', 'Фатин'), ('Атлас', 'Атлас'), ('Шифон', 'Шифон'), ('Кружево', 'Кружево'), ('Пайетки', 'Пайетки'), ('Бисер', 'Бисер'), ('Вышивка', 'Вышивка')], max_length=10, verbose_name='Ткань')),
            ],
            options={
                'verbose_name': 'Ткань',
                'verbose_name_plural': 'Ткани',
            },
        ),
        migrations.CreateModel(
            name='DressImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('photo', models.ImageField(upload_to='photos/dresses/%Y/%m/%d', verbose_name='Фотография')),
                ('dress_photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='dress.dress', verbose_name='Синхронизация')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
                'ordering': ['id', 'title'],
            },
        ),
        migrations.AddField(
            model_name='dress',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dress.dresscategory', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='dress',
            name='color',
            field=models.ManyToManyField(to='dress.color', verbose_name='Цвет'),
        ),
        migrations.AddField(
            model_name='dress',
            name='size',
            field=models.ManyToManyField(to='dress.size', verbose_name='Размер'),
        ),
        migrations.AddField(
            model_name='dress',
            name='textile',
            field=models.ManyToManyField(to='dress.textile', verbose_name='Ткань'),
        ),
    ]