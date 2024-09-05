from django.urls import path

from .views import Dresses, DressesCategory, LookDress, SearchDress, dress_update_rating

urlpatterns = [
    path('dresses/', Dresses.as_view(), name='dresses'),
    path('dresses_category/<slug:cat_slug>/', DressesCategory.as_view(), name='dresses_category'),
    path('look_dress/<slug:dress_slug>/', LookDress.as_view(), name='look_dress'),
    path('search/', SearchDress.as_view(), name='search'),
    path('dress_update_rating/<int:dress_id>/', dress_update_rating, name='dress_update_rating'),
]
