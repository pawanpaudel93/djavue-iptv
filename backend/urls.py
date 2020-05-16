"""djavue-IPTV URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from backend.api import urls as api_urls

urlpatterns = [
    path('', TemplateView.as_view(template_name='api/index.html'), name='index'),
    path('api/', include(api_urls)),
    path('admin/', admin.site.urls),
]
