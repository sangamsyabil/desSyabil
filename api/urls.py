from django.urls import path, include

urlpatterns = [
    path("products/", include("products.api.urls")),
]
