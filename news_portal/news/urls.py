from django.urls import path

from news.views import *

urlpatterns = [
    path('', AllNews.as_view(), name='index'),
    path('<int:pk>', DetailNews.as_view(), name='news'),
    path('news/search/', SearchNews.as_view(), name='search'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/edit/', NewsEdit.as_view(), name='news_edit'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('articles/create/', ArticleCreate.as_view(), name='articles_create'),
    path('articles/<int:pk>/edit/', ArticleEdit.as_view(), name='articles_edit'),
    path('articles/<int:pk>/delete/', ArticleDelete.as_view(), name='articles_delete'),
]
