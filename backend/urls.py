"""DjaVue-IPTV URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from backend.api import urls as api_urls
from backend.api.views import PlayerView

urlpatterns = [
    path('api/', include(api_urls)),
    path('admin/', admin.site.urls),
    path('player', PlayerView.as_view(), name='player'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path("api/accounts/", include("backend.accounts.urls")),
    re_path(r'^.*$', TemplateView.as_view(template_name='api/index.html'), name='index')
]
