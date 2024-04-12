from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from gallery import settings


def message_from_feedback(first_name, last_name, email, subject, message):
    message = render_to_string('main/email/feedback_email_send.html', {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'subject': subject,
        'message': message
    })
    email = EmailMessage(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.EMAIL_ADMIN])
    email.send(fail_silently=False)
