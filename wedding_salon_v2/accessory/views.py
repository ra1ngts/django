import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView

from .models import Accessory
from services.utils import DataMixin


class Accessories(DataMixin, ListView):
    model = Accessory
    template_name = 'accessory/index.html'
    context_object_name = 'accessories'
    paginate_by = 9

    def get_queryset(self):
        return Accessory.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title='Аксессуары')


class AccessoriesCategory(DataMixin, ListView):
    model = Accessory
    template_name = 'accessory/index.html'
    context_object_name = 'accessories'
    paginate_by = 9
    allow_empty = False

    def get_queryset(self):
        return Accessory.objects.filter(acat__slug=self.kwargs['acat_slug'], is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=f'Аксессуары / Категория / {context['accessories'][0].acat}')


class LookAccessory(DataMixin, DetailView):
    model = Accessory
    template_name = 'accessory/look_accessory.html'
    slug_url_kwarg = 'accessory_slug'
    context_object_name = 'accessory'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context['accessory'])


@require_POST
def accessory_update_rating(request, accessory_id):
    accessory = get_object_or_404(Accessory, id=accessory_id)
    data = json.loads(request.body)
    action = data.get('action')

    if action == 'like':
        accessory.rating += 1
    elif action == 'dislike':
        accessory.rating -= 1

    accessory.save()
    return JsonResponse({'rating': accessory.rating})
