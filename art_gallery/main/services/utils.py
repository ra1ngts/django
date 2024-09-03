from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['heart'] = mark_safe('<i class="icon-heart-o" aria-hidden="true"></i>')
        context['email_link'] = mark_safe('<a href="mailto:example@mail.com" target="_blank">' + _('папы') + '</a>')
        if 'selected' not in context:
            context['selected'] = 0
        return context
