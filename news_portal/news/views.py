from rest_framework import viewsets
import pytz
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.models import Group
from django.core.cache import cache
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django_filters.views import FilterView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from news.filters import SearchFilter
from news.forms import NewsForm
from news.models import Post, Category, Author, Comment
from django.utils.translation import gettext as _

from news.serializers import NewsArticleSerializer


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
        context['current_time'] = timezone.now()
        context['timezones'] = pytz.common_timezones
        return context

    def post(self, request):
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('index')


class DetailNews(DetailView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'detail_news'
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post_comment=Post.objects.get(id=self.kwargs['pk']))
        context['current_time'] = timezone.now()
        context['timezones'] = pytz.common_timezones
        return context

    def get_object(self, *args, **kwargs):
        obj = cache.get(f'show_news: {self.kwargs["pk"]}', None)

        if not obj:
            obj = super().get_object(queryset=self.queryset)
            cache.set(f'show_news: {self.kwargs["pk"]}', obj)

        return obj

    def post(self, request, pk):
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('news', pk)


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
        context['current_time'] = timezone.now()
        context['timezones'] = pytz.common_timezones
        return context

    def post(self, request):
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('search')


class NewsCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    form_class = NewsForm
    model = Post
    template_name = 'news_create.html'

    def form_valid(self, form):
        choice_news = form.save(commit=False)
        choice_news.choice_post = 'НОВОСТЬ'
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_time'] = timezone.now()
        context['timezones'] = pytz.common_timezones
        return context

    def post(self, request):
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('news_create')


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
        context['current_time'] = timezone.now()
        context['timezones'] = pytz.common_timezones
        return context

    def post(self, request, pk):
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('news_edit', pk)


class NewsDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = ('news.delete_post',)
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_time'] = timezone.now()
        context['timezones'] = pytz.common_timezones
        return context

    def post(self, request, pk):
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('news_delete', pk)


class ArticleCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    form_class = NewsForm
    model = Post
    template_name = 'articles_create.html'

    def form_valid(self, form):
        choice_news = form.save(commit=False)
        choice_news.choice_post = 'СТАТЬЯ'
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_time'] = timezone.now()
        context['timezones'] = pytz.common_timezones
        return context

    def post(self, request):
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('articles_create')


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
        context['current_time'] = timezone.now()
        context['timezones'] = pytz.common_timezones
        return context

    def post(self, request, pk):
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('articles_edit', pk)


class ArticleDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = ('news.delete_post',)
    model = Post
    template_name = 'articles_delete.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_time'] = timezone.now()
        context['timezones'] = pytz.common_timezones
        return context

    def post(self, request, pk):
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('articles_delete', pk)


class CategoryListView(ListView):
    model = Post
    template_name = 'category_list.html'
    context_object_name = 'category_news_list'
    paginate_by = 10

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(categories_post=self.category).order_by('-date_post')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.category.subscribers.all()
        context['is_subscriber'] = self.request.user in self.category.subscribers.all()
        context['categories_post'] = self.category
        context['current_time'] = timezone.now()
        context['timezones'] = pytz.common_timezones
        return context

    def post(self, request, pk):
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('category_list', pk)


class NewsArticlePaginator(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10000


class NewsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(choice_post='НОВОСТЬ')
    serializer_class = NewsArticleSerializer
    permission_classes = (IsAuthenticated,)  # IsAuthenticatedOrReadOnly
    pagination_class = NewsArticlePaginator


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(choice_post='СТАТЬЯ')
    serializer_class = NewsArticleSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = NewsArticlePaginator


@login_required
def be_author(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        authors_group.user_set.add(user)
        Author.objects.create(author_user_id=request.user.pk)
    return redirect('index')


@login_required
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)

    message = _('вы успешно подписались на рассылку новостей в категории:')
    return render(request, 'subscribe.html', {'user': user, 'category': category, 'message': message})


@login_required
def un_subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.remove(user)

    message = _('вы отписались от рассылки новостей в категории:')
    return render(request, 'subscribe.html', {'user': user, 'category': category, 'message': message})


@login_required
def like_post(request, pk):
    post = Post.objects.get(id=pk)
    post.like()
    post.author_post.update_rating()
    return redirect(f'/news/{post.pk}')


@login_required
def dislike_post(request, pk):
    post = Post.objects.get(id=pk)
    post.dislike()
    post.author_post.update_rating()
    return redirect(f'/news/{post.pk}')


def permission_denied_error(request, exception=None):
    return render(request, '403.html', status=403)


def index_redirect(request):
    return HttpResponseRedirect('news')
