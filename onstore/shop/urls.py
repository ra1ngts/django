from django.urls import path

from shop.views import product_list, product_category, product_detail, about

urlpatterns = [
    path('', product_list, name='product_list'),
    path('<slug:category_slug>/', product_category, name='category'),
    path('product/<slug:product_slug>/', product_detail, name='product'),
    path('about/', about, name='about'),
]
