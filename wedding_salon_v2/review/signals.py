from django.core.mail import EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from wedding_salon import settings
from .models import Review


@receiver(post_save, sender=Review)
def notification_about_review(sender, instance, created, **kwargs):
    if created:
        name = instance.name
        review = instance.review
        subject = f'Новый отзыв от {name}'
        message = render_to_string('email/new_review.html', context={
            'name': name,
            'review': review,
        })
        email = EmailMessage(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.EMAIL_ADMIN])
        email.content_subtype = 'html'
        email.send(fail_silently=False)
