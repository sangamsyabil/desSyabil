from django.urls import path, include
from rest_framework.routers import DefaultRouter


from products.api.views import ProductViewSet, CategoryViewSet

router = DefaultRouter()
router.register("", ProductViewSet)
router.register("categories/", CategoryViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
