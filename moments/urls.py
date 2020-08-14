from django.urls import path
from .views import (
    IndexView,
    ReturnPolicyView,
    PrivacyPolicyView,
    DeliveryPolicyView,
    CookiePolicyView,
    TermsView,
    FaqView,
    ContactUsView,
    TradeShowsView,
)


app_name = 'moments'


urlpatterns = [
    path('', IndexView.as_view(), name='home'),

    path('trade-shows/', TradeShowsView.as_view(), name='trade-shows'),
    path('return-policy/', ReturnPolicyView.as_view(), name='return-policy'),
    path('delivery-policy/', DeliveryPolicyView.as_view(), name='delivery-policy'),
    path('privacy-policy/', PrivacyPolicyView.as_view(), name='privacy-policy'),
    path('cookie-policy/', CookiePolicyView.as_view(), name='cookie-policy'),
    path('contact-us/', ContactUsView.as_view(), name='contact-us'),
    path('terms/', TermsView.as_view(), name='terms'),
    path('faq/', FaqView.as_view(), name='faq'),
]
