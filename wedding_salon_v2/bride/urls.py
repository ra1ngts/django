from django.urls import path

from .views import Brides, BridesCategory, LookBride

urlpatterns = [
    path('brides/', Brides.as_view(), name='brides'),
    path('brides_category/<slug:cat_brides_slug>/', BridesCategory.as_view(), name='brides_category'),
    path('look_bride/<slug:bride_slug>/', LookBride.as_view(), name='look_bride'),
]
