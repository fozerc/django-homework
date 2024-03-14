"""
URL configuration for django_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include
from django_app.views import main, create, password, change_data, deactivate, register, login, logout, username

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('about/', include('django_app.about_url')),
    path('create', create),
    path('topics/', include('django_app.topics_url')),
    path('set-password', password),
    path('set-userdata', change_data),
    path('deactivate', deactivate),
    path('register', register),
    path('login', login),
    path('logout', logout),
    path('profile/<str:pk>', username)
]
