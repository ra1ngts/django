import datetime

from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

from django.template.loader import render_to_string

from news.models import Post, Category


@shared_task
def send_notifications_task(preview, pk, title_post, subscribers):
    html_content = render_to_string('post_created_email.html',
                                    {'text_post': preview,
                                     'link': f'{settings.SITE_URL}/news/{pk}'})

    msg = EmailMultiAlternatives(subject=title_post, body='', from_email=settings.DEFAULT_FROM_EMAIL, to=subscribers)
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
    print('Уведомление о новой статье отправлено на почту')


@shared_task
def send_weekly_notifications_task():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(date_post__gte=last_week)
    categories = set(posts.values_list('categories_post__title_category', flat=True))
    subscribers = set(
        Category.objects.filter(title_category__in=categories).values_list('subscribers__email', flat=True))
    html_content = render_to_string('weekly_news.html',
                                    {'link': settings.SITE_URL, 'posts': posts})

    msg = EmailMultiAlternatives(subject='Статьи за неделю!', body='', from_email=settings.DEFAULT_FROM_EMAIL,
                                 to=subscribers)
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
    print('Еженедельная рассылка новостей отправлена на почту')
