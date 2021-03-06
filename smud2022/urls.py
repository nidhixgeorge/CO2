"""smud2022 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from co2 import views
from django.contrib.auth import views as auth_views
from django.urls import path, re_path,include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('privacy', views.show_privacy, name='privacy'),
    path('terms', views.show_terms, name='terms'),
    path('contactus', views.contactus, name='contactus'),
]
