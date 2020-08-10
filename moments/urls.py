from django.urls import path
from .views import IndexView


app_name = 'moments'


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
]
