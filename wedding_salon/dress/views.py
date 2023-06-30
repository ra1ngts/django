from django.core.paginator import Paginator
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django_filters.views import FilterView

from accessory.models import Accessory
from brides.models import Bride
from contacts.models import Contacts
from dress.filters import SearchFilter
from dress.models import Dress
from review.forms import AddReviewForm
from review.models import Review

menu = [{'title': 'Невесты', 'url_name': 'brides'},
        {'title': 'Отзывы', 'url_name': 'reviews'},
        {'title': 'Контакты', 'url_name': 'contacts'},
        {'title': 'Поиск платьев', 'url_name': 'dresses_search'},
        ]


class Dresses(ListView):
    model = Dress
    template_name = 'dress/index.html'
    context_object_name = 'dresses'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Свадебные платья'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Dress.objects.filter(is_published=True)


class DressesCategory(ListView):
    model = Dress
    template_name = 'dress/index.html'
    context_object_name = 'dresses'
    allow_empty = False

    def get_queryset(self):
        return Dress.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Категория: ' + str(context['dresses'][0].cat)
        context['cat_selected'] = context['dresses'][0].cat_id
        return context


class LookDress(DetailView):
    model = Dress
    template_name = 'dress/dress.html'
    slug_url_kwarg = 'dress_slug'
    context_object_name = 'dress'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['dress']
        context['cat_selected'] = context['dress'].cat_id
        return context


class SearchDress(FilterView):
    model = Dress
    template_name = 'dress/dresses_search.html'
    context_object_name = 'dresses_search'
    filterset_class = SearchFilter
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = SearchFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Поиск платьев'
        context['filterset'] = self.filterset
        return context


class Accessories(ListView):
    model = Accessory
    template_name = 'accessory/accessories.html'
    context_object_name = 'accessories'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Аксессуары'
        context['acat_selected'] = 0
        return context

    def get_queryset(self):
        return Accessory.objects.filter(is_published=True)


class AccessoriesCategory(ListView):
    model = Accessory
    template_name = 'accessory/accessories.html'
    context_object_name = 'accessories'
    allow_empty = False

    def get_queryset(self):
        return Accessory.objects.filter(acat__slug=self.kwargs['acat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Категория: ' + str(context['accessories'][0].acat)
        context['acat_selected'] = context['accessories'][0].acat_id
        return context


class LookAccessory(DetailView):
    model = Accessory
    template_name = 'accessory/accessory.html'
    slug_url_kwarg = 'accessory_slug'
    context_object_name = 'accessory'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['accessory']
        context['acat_selected'] = context['accessory'].acat_id
        return context


class Brides(ListView):
    model = Bride
    template_name = 'brides/brides.html'
    context_object_name = 'brides'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Невесты'
        context['bcat_selected'] = 0
        return context

    def get_queryset(self):
        return Bride.objects.filter(is_published=True)


class BridesCategory(ListView):
    model = Bride
    template_name = 'brides/brides.html'
    context_object_name = 'brides'
    allow_empty = False

    def get_queryset(self):
        return Bride.objects.filter(bcat__slug=self.kwargs['bcat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Категория: ' + str(context['brides'][0].bcat)
        context['bcat_selected'] = context['brides'][0].bcat_id
        return context


class LookBride(DetailView):
    model = Bride
    template_name = 'brides/bride.html'
    slug_url_kwarg = 'bride_slug'
    context_object_name = 'bride'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['bride']
        context['bcat_selected'] = context['bride'].bcat_id
        return context


def reviews(request):
    review = Review.objects.all()
    paginator = Paginator(review, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST':
        form = AddReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews')
    else:
        form = AddReviewForm()

    context = {'form': form,
               'review': review,
               'menu': menu,
               'title': 'Отзывы',
               'page_obj': page_obj
               }

    return render(request, 'review/reviews.html', context=context)


class Contact(ListView):
    model = Contacts
    template_name = 'contacts/contacts.html'
    context_object_name = 'contacts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Контакты'
        return context


def dress_like(request, dress_slug):
    like = Dress.objects.get(slug=dress_slug)
    like.like()
    return redirect(f'/look_dress/{like.slug}')


def dress_dislike(request, dress_slug):
    dislike = Dress.objects.get(slug=dress_slug)
    dislike.dislike()
    return redirect(f'/look_dress/{dislike.slug}')


def accessory_like(request, accessory_slug):
    like = Accessory.objects.get(slug=accessory_slug)
    like.like()
    return redirect(f'/look_accessory/{like.slug}')


def accessory_dislike(request, accessory_slug):
    dislike = Accessory.objects.get(slug=accessory_slug)
    dislike.dislike()
    return redirect(f'/look_accessory/{dislike.slug}')


def index_redirect(request):
    return HttpResponseRedirect('dresses')


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
