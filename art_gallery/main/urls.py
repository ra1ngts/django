from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<int:cat_id>/', views.show_gallery, name='show_gallery'),
    path('<int:img_id>/', views.show_image, name='show_image'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('success/', views.success, name='success'),
]
