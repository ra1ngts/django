from django.urls import path

from dress.views import *

urlpatterns = [
    path('dresses/', Dresses.as_view(), name='home'),
    path('dresses_category/<slug:cat_slug>/', DressesCategory.as_view(), name='dresses_category'),
    path('look_dress/<slug:dress_slug>/', LookDress.as_view(), name='look_dress'),
    path('look_dress/<slug:dress_slug>/like/', dress_like, name='dress_like'),
    path('look_dress/<slug:dress_slug>/dislike/', dress_dislike, name='dress_dislike'),
    path('dresses/search/', SearchDress.as_view(), name='dresses_search'),
    path('accessories/', Accessories.as_view(), name='accessories'),
    path('accessories_category/<slug:acat_slug>/', AccessoriesCategory.as_view(), name='accessories_category'),
    path('look_accessory/<slug:accessory_slug>/', LookAccessory.as_view(), name='look_accessory'),
    path('brides/', Brides.as_view(), name='brides'),
    path('brides_category/<slug:cat_brides_slug>/', BridesCategory.as_view(), name='brides_category'),
    path('look_bride/<slug:bride_slug>/', LookBride.as_view(), name='look_bride'),
    path('reviews/', reviews, name='reviews'),
    path('contacts/', Contact.as_view(), name='contacts'),
]
