from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from wedding_salon import settings


def message_from_feedback(name, email, message):
    subject = f'Новое сообщение от {name}'
    message = render_to_string('email/new_feedback.html', {
        'name': name,
        'email': email,
        'message': message,
        'subject': subject,
    })
    email = EmailMessage(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.EMAIL_ADMIN])
    email.content_subtype = 'html'
    email.send(fail_silently=False)
