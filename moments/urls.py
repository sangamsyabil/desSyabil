from django.conf.urls import url
from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.generic import RedirectView

from accounts.views import LoginView, RegisterView, GuestRegisterView
from addresses.views import (
    AddressCreateView,
    AddressListView,
    AddressUpdateView,
    checkout_address_create_view,
    checkout_address_reuse_view
)
from analytics.views import SalesView, SalesAjaxView
from billing.views import payment_method_view, payment_method_createview
from carts.views import cart_detail_api_view
from marketing.views import MarketingPreferenceUpdateView, MailchimpWebhookView
from orders.views import LibraryView
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


    path('address/', RedirectView.as_view(url='/addresses')),
    path('addresses/', AddressListView.as_view(), name='addresses'),
    path('addresses/create/', AddressCreateView.as_view(), name='address-create'),
    url(r'^addresses/(?P<pk>\d+)/$', AddressUpdateView.as_view(), name='address-update'),
    path('analytics/sales/', SalesView.as_view(), name='sales-analytics'),
    path('analytics/sales/data/', SalesAjaxView.as_view(), name='sales-analytics-data'),
    path('login/', LoginView.as_view(), name='login'),
    path('checkout/address/create/', checkout_address_create_view, name='checkout_address_create'),
    path('checkout/address/reuse/', checkout_address_reuse_view, name='checkout_address_reuse'),
    path('register/guest/', GuestRegisterView.as_view(), name='guest_register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api/cart/', cart_detail_api_view, name='api-cart'),
    path('billing/payment-method/', payment_method_view, name='billing-payment-method'),
    path('billing/payment-method/create/', payment_method_createview, name='billing-payment-method-endpoint'),
    path('register/', RegisterView.as_view(), name='register'),
    path('library/', LibraryView.as_view(), name='library'),
    path('settings/', RedirectView.as_view(url='/account')),
    path('settings/email/', MarketingPreferenceUpdateView.as_view(), name='marketing-pref'),
    path('webhooks/mailchimp/', MailchimpWebhookView.as_view(), name='webhooks-mailchimp'),
]
