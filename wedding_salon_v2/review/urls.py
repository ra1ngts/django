from django.urls import path

from .views import Reviews

urlpatterns = [
    path('reviews/', Reviews.as_view(), name='reviews'),
]
