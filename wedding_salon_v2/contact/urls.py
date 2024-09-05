from django.urls import path

from .views import Contacts

urlpatterns = [
    path('contacts/', Contacts.as_view(), name='contacts'),
]
