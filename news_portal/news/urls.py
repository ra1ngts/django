from django.urls import path

from news.views import AllNews, DetailNews

urlpatterns = [
    path('', AllNews.as_view()),
    path('<int:pk>', DetailNews.as_view()),
]
