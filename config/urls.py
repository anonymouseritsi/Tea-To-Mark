"""
URL Configuration for milk tea shop app.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tea_shop.urls')),
]
