from django.views.generic import ListView, DetailView

from news.models import Post


class AllNews(ListView):
    model = Post
    ordering = '-date_post'
    template_name = 'default.html'
    context_object_name = 'all_news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['amount_news'] = None
        return context


class DetailNews(DetailView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'detail_news'
