from celery import shared_task
from decouple import config
from django.core.mail import send_mail
from .models import Post


@shared_task
def post_create(post_comment_id):
    post = Post.objects.get(pk=post_comment_id)
    subject = f'Появилось новое объявление в категории "{post.category_post}"'
    message = f'На "Доске объявлений MMORPG" новое объявление "{post.title_post}" в категории "{post.category_post}".'
    mail_sent = send_mail(subject, message, config('DEFAULT_FROM_EMAIL'), [config('DEFAULT_FROM_EMAIL')])
    print('Новость отправлена на почту')
    return mail_sent
