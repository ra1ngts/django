from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView

from services.email import message_from_feedback
from services.utils import DataMixin
from .forms import FeedBackForm
from .models import Contact


class Contacts(DataMixin, FormView):
    template_name = 'contact/index.html'
    context_object_name = 'contacts'
    form_class = FeedBackForm
    success_url = reverse_lazy('contacts')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = Contact.objects.all()
        context['phone'] = '+71234567890'
        context['email'] = 'example@example.com'
        return self.get_mixin_context(context, title='Контакты')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        messages.add_message(self.request, messages.SUCCESS, 'Ваше сообщение успешно отправлено.', extra_tags='contact')
        message_from_feedback(name, email, message)
        return super().form_valid(form)
