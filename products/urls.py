from django.conf.urls import url
from django.urls import path

from .views import (
    ProductListView,
    ProductDetailView,
)

app_name = 'product'

urlpatterns = [
    path('list/', ProductListView.as_view(), name='lists'),
    path('<slug>', ProductDetailView.as_view(), name='details'),
]
