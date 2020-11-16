from django.contrib import admin
from django.urls import path, include
from api import urls, views

urlpatterns = [
    path('', include(urls)),
    path('admin/', admin.site.urls),
]
