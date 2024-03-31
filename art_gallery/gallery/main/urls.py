from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('show_image/<slug:img_slug>', views.show_image, name='show_image'),
    path('category/<slug:cat_slug>', views.category, name='category'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
]
