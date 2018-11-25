from django.urls import path

from .views import get_data, home

urlpatterns = [
    path('', home),
    path('api/data/', get_data.as_view(), name='api'),
]
