from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('category/', views.category, name='category'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('post/<int:post_id>/', views.show_image, name='show_image'),
    path('category/<int:cat_id>/', views.show_category, name='show_category')
]
