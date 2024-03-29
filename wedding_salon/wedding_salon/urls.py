"""wedding_salon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from dress import views
from dress.views import pageNotFound, DressAPI, AccessoryAPI, BrideAPI

from wedding_salon import settings

router = routers.SimpleRouter()
router.register(r'dresses', DressAPI)
router.register(r'accessory', AccessoryAPI)
router.register(r'brides', BrideAPI)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dress.urls')),
    path('', views.index_redirect),
    path('accounts/', include('allauth.urls')),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound
