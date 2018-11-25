from django.contrib import admin
from django.urls import include, path

from graph import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls)),
]
