from django.urls import path

from shop.views import ProductList, ProductCategory, ProductDetail, about

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('<slug:category_slug>/', ProductCategory.as_view(), name='category'),
    path('product/<slug:product_slug>/', ProductDetail.as_view(), name='product'),
    path('about/', about, name='about'),
]
