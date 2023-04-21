from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.models import Group
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django_filters.views import FilterView

from news.filters import SearchFilter
from news.forms import NewsForm
from news.models import Post


class AllNews(ListView):
    model = Post
    ordering = '-date_post'
    template_name = 'default.html'
    context_object_name = 'all_news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = SearchFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['amount_news'] = None
        return context


class DetailNews(DetailView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'detail_news'


class SearchNews(FilterView):
    model = Post
    ordering = '-date_post'
    template_name = 'search.html'
    context_object_name = 'search_news'
    filterset_class = SearchFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = SearchFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewsCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    form_class = NewsForm
    model = Post
    template_name = 'news_create.html'

    def form_valid(self, form):
        choice_news = form.save(commit=False)
        choice_news.choice_post = 'НОВОСТЬ'
        return super().form_valid(form)


class NewsEdit(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['not_author'] = not self.request.user.groups.filter(name='authors').exists()
        return context


class NewsDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = ('news.delete_post',)
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('index')


class ArticleCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    form_class = NewsForm
    model = Post
    template_name = 'articles_create.html'

    def form_valid(self, form):
        choice_news = form.save(commit=False)
        choice_news.choice_post = 'СТАТЬЯ'
        return super().form_valid(form)


class ArticleEdit(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
    form_class = NewsForm
    model = Post
    template_name = 'articles_edit.html'

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['not_author'] = not self.request.user.groups.filter(name='authors').exists()
        return context


class ArticleDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = ('news.delete_post',)
    model = Post
    template_name = 'articles_delete.html'
    success_url = reverse_lazy('index')


@login_required
def be_author(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        authors_group.user_set.add(user)
    return redirect('index')


def permission_denied_error(request, exception=None):
    return render(request, '403.html', status=403)
