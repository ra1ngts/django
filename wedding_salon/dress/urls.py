from django.urls import path
from django.views.decorators.cache import cache_page

from dress.views import *

urlpatterns = [
    path('dresses/', cache_page(60 * 10)(Dresses.as_view()), name='home'),
    path('dresses_category/<slug:cat_slug>/', cache_page(60 * 10)(DressesCategory.as_view()), name='dresses_category'),
    path('look_dress/<slug:dress_slug>/', LookDress.as_view(), name='look_dress'),
    path('look_dress/<slug:dress_slug>/like/', dress_like, name='dress_like'),
    path('look_dress/<slug:dress_slug>/dislike/', dress_dislike, name='dress_dislike'),
    path('dresses/search/', SearchDress.as_view(), name='dresses_search'),
    path('accessories/', Accessories.as_view(), name='accessories'),
    path('accessories_category/<slug:acat_slug>/', cache_page(60 * 10)(AccessoriesCategory.as_view()),
         name='accessories_category'),
    path('look_accessory/<slug:accessory_slug>/', LookAccessory.as_view(), name='look_accessory'),
    path('look_accessory/<slug:accessory_slug>/like/', accessory_like, name='accessory_like'),
    path('look_accessory/<slug:accessory_slug>/dislike/', accessory_dislike, name='accessory_dislike'),
    path('brides/', cache_page(60 * 10)(Brides.as_view()), name='brides'),
    path('brides_category/<slug:cat_brides_slug>/', cache_page(60 * 10)(BridesCategory.as_view()),
         name='brides_category'),
    path('look_bride/<slug:bride_slug>/', cache_page(60 * 10)(LookBride.as_view()), name='look_bride'),
    path('reviews/', reviews, name='reviews'),
    path('contacts/', cache_page(60 * 10)(Contact.as_view()), name='contacts'),
]
