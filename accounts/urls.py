from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import (
    AccountHomeView,
    AccountEmailActivateView,
    UserDetailUpdateView,
    LoginView,
    GuestRegisterView,
    RegisterView,
)

app_name = 'account'

urlpatterns = [
    path('', AccountHomeView.as_view(), name='account_home'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/guest/', GuestRegisterView.as_view(), name='guest_register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('details/', UserDetailUpdateView.as_view(), name='user-update'),
    path('email/confirm/(?P<key>[0-9A-Za-z]+)/$', AccountEmailActivateView.as_view(), name='email-activate'),
    path('email/resend-activation/$', AccountEmailActivateView.as_view(), name='resend-activation'),
]
