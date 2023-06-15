from datetime import datetime

from django.core.management.base import BaseCommand, CommandError

from news.models import Category, Post


class Command(BaseCommand):
    help = 'Удаление всех новостей из выбранной категории.'
    requires_migrations_checks = True

    def handle(self, *args, **options):
        self.stdout.write()
        self.stdout.write('*' * 26)
        self.stdout.write('*** КАТЕГОРИИ НОВОСТЕЙ ***')
        self.stdout.write('*' * 26)
        self.stdout.write()
        for news in Category.objects.all():
            self.stdout.write(f'{news.id} : {news.title_category}')
        self.stdout.write()
        answer = int(input('Введите номер категории для удаления всех новостей: '))
        for category in Category.objects.all():
            if answer == 1 and category.id == 1:
                self.stdout.write(f'Вы уверены что хотите удалить все новости из категории {category.title_category}?')
                answer_2 = input('Введите "да" для подтверждения или иное для выхода: ')
                if answer_2 == 'да':
                    category = Category.objects.get(pk=1)
                    Post.objects.filter(categories_post=category).delete()
                    self.stdout.write(
                        self.style.SUCCESS(f'Все новости из категории {category.title_category} удалены!'))
                    return
                self.stdout.write(self.style.ERROR('Выход из программы'))
            elif answer == 2 and category.id == 2:
                self.stdout.write(f'Вы уверены что хотите удалить все новости из категории {category.title_category}?')
                answer_2 = input('Введите "да" для подтверждения или иное для выхода: ')
                if answer_2 == 'да':
                    category = Category.objects.get(pk=2)
                    Post.objects.filter(categories_post=category).delete()
                    self.stdout.write(
                        self.style.SUCCESS(f'Все новости из категории {category.title_category} удалены!'))
                    return
                self.stdout.write(self.style.ERROR('Выход из программы'))
            elif answer == 3 and category.id == 3:
                self.stdout.write(f'Вы уверены что хотите удалить все новости из категории {category.title_category}?')
                answer_2 = input('Введите "да" для подтверждения или иное для выхода: ')
                if answer_2 == 'да':
                    category = Category.objects.get(pk=3)
                    Post.objects.filter(categories_post=category).delete()
                    self.stdout.write(
                        self.style.SUCCESS(f'Все новости из категории {category.title_category} удалены!'))
                    return
                self.stdout.write(self.style.ERROR('Выход из программы'))
            elif answer == 4 and category.id == 4:
                self.stdout.write(f'Вы уверены что хотите удалить все новости из категории {category.title_category}?')
                answer_2 = input('Введите "да" для подтверждения или иное для выхода: ')
                if answer_2 == 'да':
                    category = Category.objects.get(pk=4)
                    Post.objects.filter(categories_post=category).delete()
                    self.stdout.write(
                        self.style.SUCCESS(f'Все новости из категории {category.title_category} удалены!'))
                    return
                self.stdout.write(self.style.ERROR('Выход из программы'))
            elif answer == 5 and category.id == 5:
                self.stdout.write(f'Вы уверены что хотите удалить все новости из категории {category.title_category}?')
                answer_2 = input('Введите "да" для подтверждения или иное для выхода: ')
                if answer_2 == 'да':
                    category = Category.objects.get(pk=5)
                    Post.objects.filter(categories_post=category).delete()
                    self.stdout.write(
                        self.style.SUCCESS(f'Все новости из категории {category.title_category} удалены!'))
                    return
                self.stdout.write(self.style.ERROR('Выход из программы'))
