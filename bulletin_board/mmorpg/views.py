from decouple import config
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django_filters.views import FilterView

from mmorpg.filters import SearchFilter
from mmorpg.forms import PostForm, CommentForm
from mmorpg.models import Post, Comment
from mmorpg.tasks import post_create


class Posts(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    ordering = '-date_post'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['amount_posts'] = None
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post_detail'


class PostCreate(CreateView):
    model = Post
    template_name = 'post_create.html'
    form_class = PostForm

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.method == 'POST':
            post.author_post, created = User.objects.get_or_create(id=self.request.user.id)
            post.save()
            post_create(post_comment_id=post.id)
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostEdit(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    form_class = PostForm

    def get_template_names(self):
        post = self.get_object()
        if post.author_post == self.request.user:
            self.template_name = 'post_edit.html'
            return self.template_name
        else:
            raise PermissionDenied


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts')

    def get_template_names(self):
        post = self.get_object()
        if post.author_post == self.request.user:
            self.template_name = 'post_delete.html'
            return self.template_name
        else:
            raise PermissionDenied


class Profile(ListView):
    model = Comment
    template_name = 'profile.html'


class Search(FilterView):
    model = Post
    ordering = '-date_post'
    template_name = 'filter.html'
    context_object_name = 'search'
    filterset_class = SearchFilter

    def get_queryset(self):
        queryset = super().get_queryset().filter(author_post=self.request.user)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class Comments(ListView):
    model = Comment
    template_name = 'comments.html'
    context_object_name = 'comments'
    ordering = '-date_comment'
    paginate_by = 5

    def get_queryset(self):
        queryset = Comment.objects.filter(post_comment__author_post=self.request.user)
        return queryset


class CommentCreate(CreateView):
    model = Comment
    template_name = 'comment_create.html'
    form_class = CommentForm
    success_url = '/comments/'

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.author_comment = User.objects.get(id=self.request.user.id)
        comment.post_comment = Post.objects.get(id=self.kwargs['pk'])
        comment.save()
        result = super().form_valid(form)
        send_mail(
            subject=f'Новый комментарий у вашего объявления "{comment.post_comment.title_post}"',
            message=f'Комментарий от {comment.author_comment}: "{comment.text_comment}"',
            from_email=config('DEFAULT_FROM_EMAIL'),
            recipient_list=[config('DEFAULT_FROM_EMAIL')]
        )
        return result


class CommentDetail(DetailView):
    model = Comment
    template_name = 'comment_detail.html'
    context_object_name = 'comment_detail'

    def get_template_names(self):
        response = self.get_object()
        if response.post_comment.author_post == self.request.user:
            self.template_name = 'comment_detail.html'
            return self.template_name
        else:
            raise PermissionDenied


@login_required()
def confirm_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    comment.confirmation_comment = True
    comment.save()
    send_mail(
        subject=f'Принят комментарий от {comment.author_comment}',
        message=f'Принят комментарий от {comment.author_comment} к объявлению "{comment.post_comment.title_post}"',
        from_email=config('DEFAULT_FROM_EMAIL'),
        recipient_list=[config('DEFAULT_FROM_EMAIL')]
    )
    return render(request, 'accept.html')


@login_required()
def reject_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    comment.confirmation_comment = False
    comment.save()
    return HttpResponseRedirect(reverse('comments'))


def permission_denied_error(request, exception=None):
    return render(request, '403.html', status=403)
