from django.conf.urls import url
from django.urls import path

from .views import (
    ProductListView,
    ProductDetailSlugView,
    # ProductDownloadView
)

app_name = 'products'

urlpatterns = [
    path('list/', ProductListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),
    # url(r'^(?P<slug>[\w-]+)/(?P<pk>\d+)/$', ProductDownloadView.as_view(), name='download'),
]
