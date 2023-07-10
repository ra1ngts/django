from celery import shared_task
from decouple import config
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import Post


@shared_task
def post_create(post_comment_id):
    post = Post.objects.get(pk=post_comment_id)
    html_content = render_to_string('post_create_email.html',
                                    {'link': f'{config("SITE_URL")}/{post_comment_id}'})

    msg = EmailMultiAlternatives(subject=f'На "Доске объявлений MMORPG" новое объявление - {post.title_post}', body='',
                                 from_email=config('DEFAULT_FROM_EMAIL'),
                                 to=[config('DEFAULT_FROM_EMAIL')])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
    print('Уведомление о новом объявлении отправлено на почту')
