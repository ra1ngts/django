from django.urls import path

from .views import Accessories, AccessoriesCategory, LookAccessory, accessory_update_rating

urlpatterns = [
    path('accessories/', Accessories.as_view(), name='accessories'),
    path('accessories_category/<slug:acat_slug>/', AccessoriesCategory.as_view(), name='accessories_category'),
    path('look_accessory/<slug:accessory_slug>/', LookAccessory.as_view(), name='look_accessory'),
    path('accessory_update_rating/<int:accessory_id>/', accessory_update_rating, name='accessory_update_rating'),
]
