import json

from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView

from django_filters.views import FilterView

from .filters import SearchFilter
from .models import Dress
from services.utils import DataMixin


class Dresses(DataMixin, ListView):
    model = Dress
    template_name = 'dress/index.html'
    context_object_name = 'dresses'
    paginate_by = 9

    def get_queryset(self):
        return Dress.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title='Свадебные платья')


class DressesCategory(DataMixin, ListView):
    model = Dress
    template_name = 'dress/index.html'
    context_object_name = 'dresses'
    paginate_by = 9
    allow_empty = False

    def get_queryset(self):
        return Dress.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=f'Свадебные платья / Категория / {context['dresses'][0].cat}')


class LookDress(DataMixin, DetailView):
    model = Dress
    template_name = 'dress/look_dress.html'
    slug_url_kwarg = 'dress_slug'
    context_object_name = 'dress'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['phone'] = '+71234567890'
        return self.get_mixin_context(context, title=context['dress'])


class SearchDress(DataMixin, FilterView):
    model = Dress
    template_name = 'dress/search.html'
    context_object_name = 'search'
    filterset_class = SearchFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = SearchFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return self.get_mixin_context(context, title='Поиск')


@require_POST
def dress_update_rating(request, dress_id):
    dress = get_object_or_404(Dress, id=dress_id)
    data = json.loads(request.body)
    action = data.get('action')

    if action == 'like':
        dress.rating += 1
    elif action == 'dislike':
        dress.rating -= 1

    dress.save()
    return JsonResponse({'rating': dress.rating})


def index_redirect(request):
    return HttpResponseRedirect('dresses')
