from django.urls import path

from . import views
from .views import Index, ShowGallery, Information

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('<int:category_id>/', ShowGallery.as_view(), name='show_gallery'),
    path('about/', Information.as_view(), name='about'),
    path('contacts/', views.contacts, name='contacts')
]
