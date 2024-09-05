from django.urls import path

from .views import (UsersSignupView, UsersLoginView, UsersLogoutView,
                    PasswordsChangeView, PasswordsResetView, PasswordsResetFromKeyView, PasswordsResetDoneView,
                    UsersProfileView)

urlpatterns = [
    path('signup/', UsersSignupView.as_view(), name='signup'),
    path('login/', UsersLoginView.as_view(), name='login'),
    path('logout/', UsersLogoutView.as_view(), name='logout'),
    path('change_password/', PasswordsChangeView.as_view(), name='change_password'),
    path('reset_password/', PasswordsResetView.as_view(), name='reset_password'),
    path('reset_key_password/<uidb36>/<key>/', PasswordsResetFromKeyView.as_view(), name='reset_key_password'),
    path('reset_done_password/', PasswordsResetDoneView.as_view(), name='reset_done_password'),
    path('profile/', UsersProfileView.as_view(), name='profile'),
]
