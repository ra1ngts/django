from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<int:cat_id>/', views.show_gallery, name='show_gallery'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts')
]
