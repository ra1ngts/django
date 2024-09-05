"""
URL configuration for wedding_salon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import utils.exception_handlers
from dress import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('captcha/', include('captcha.urls')),
    path('', include('accessory.urls')),
    path('', include('bride.urls')),
    path('', include('contact.urls')),
    path('', include('dress.urls')),
    path('', include('review.urls')),
    path('', include('user.urls')),
    path('', views.index_redirect),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler403 = utils.exception_handlers.e_handler403
handler404 = utils.exception_handlers.e_handler404
handler500 = utils.exception_handlers.e_handler500
