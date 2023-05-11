from django.urls import path
from django.views.decorators.cache import cache_page

from news.views import *

urlpatterns = [
    path('news/', cache_page(60)(AllNews.as_view()), name='index'),
    path('news/<int:pk>/', cache_page(60 * 5)(DetailNews.as_view()), name='news'),
    path('news/<int:pk>/like/', like_post, name='like_post'),
    path('news/<int:pk>/dislike/', dislike_post, name='dislike_post'),
    path('news/search/', SearchNews.as_view(), name='search'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/edit/', NewsEdit.as_view(), name='news_edit'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('articles/create/', ArticleCreate.as_view(), name='articles_create'),
    path('articles/<int:pk>/edit/', ArticleEdit.as_view(), name='articles_edit'),
    path('articles/<int:pk>/delete/', ArticleDelete.as_view(), name='articles_delete'),
    path('be_author/', be_author, name='be_author'),
    path('categories/<int:pk>/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribe/', subscribe, name='subscribe'),
    path('categories/<int:pk>/un_subscribe/', un_subscribe, name='un_subscribe'),
]
