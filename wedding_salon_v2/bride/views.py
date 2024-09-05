from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Bride
from dress.models import Dress
from services.utils import DataMixin


class Brides(DataMixin, ListView):
    model = Bride
    template_name = 'brides/index.html'
    context_object_name = 'brides'
    paginate_by = 9

    def get_queryset(self):
        return Bride.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title='Невесты')


class BridesCategory(DataMixin, ListView):
    model = Bride
    template_name = 'brides/index.html'
    context_object_name = 'brides'
    paginate_by = 9
    allow_empty = False

    def get_queryset(self):
        return Bride.objects.filter(bcat__slug=self.kwargs['cat_brides_slug'], is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=f'Невесты / Категория / {context['brides'][0].bcat}')


class LookBride(DataMixin, DetailView):
    model = Bride
    template_name = 'brides/look_bride.html'
    slug_url_kwarg = 'bride_slug'
    context_object_name = 'bride'

    def dress_available(self, bride_slug):
        bride = get_object_or_404(Bride, slug=bride_slug)
        dress = Dress.objects.filter(slug=bride.slug).first()
        return dress

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bride_slug = self.kwargs.get(self.slug_url_kwarg)
        dress = self.dress_available(bride_slug)
        context['dress'] = dress
        context.update(self.get_mixin_context(context, title=context['bride']))
        return context
