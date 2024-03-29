"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.urls import re_path
from django.views.generic import TemplateView
from carapp import views

urlpatterns = [
    path('', views.index, name='home'),
    re_path(r'^about', TemplateView.as_view(template_name="carapp/about.html"), name='about'),
    re_path(r'^contacts', TemplateView.as_view(template_name="carapp/contacts.html"), name='contacts'),
    # re_path(r'^users/(?P<id>\d+)/(?P<name>\D+)/',views.users),
    path('users/', views.users),
    path('personas/', views.personas),
    path('details/', views.details),
    path('users/<int:id>/<str:name>/', views.users),
    re_path(r'^products/$', views.products),
    re_path(r'^products/(?P<productid>\d+)/', views.products),
    path('admin/', admin.site.urls),
]