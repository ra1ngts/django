from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from news.models import PostCategory
from news.tasks import send_notifications_task


@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.categories_post.all()
        subscribers: list[str] = []
        for category in categories:
            subscribers += category.subscribers.all()

        subscribers = [s.email for s in subscribers]

        send_notifications_task.delay(instance.text_post, instance.pk, instance.title_post, subscribers)
