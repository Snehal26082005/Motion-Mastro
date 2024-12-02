"""
URL configuration for PlaystationLite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from . import views

urlpatterns = [
    path('index',views.index,name='index'),
    path('',views.login,name='login'),
    path('hcr', views.hcr, name='hcr'),
    path('tet', views.tet, name='tet'),
    path('carsi', views.carsi, name='carsi'),
    path('mbi', views.mbi, name='mbi'),
    path('ssurf', views.ssurf, name='ssurf'),
    path('signup',views.signup,name='signup'),
    path('feedback',views.feedback,name='feedback'),


]
