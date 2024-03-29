"""
URL configuration for btrs project.

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
from django.urls import path
from bus_enquiry.views import *;

urlpatterns = [
    path('', home, name='home'),
    path('login/', user_login, name='login'),
    path('register/',user_register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('findbus/', findbus, name='findbus'),
    path('success/', success, name='success'),
    path('bookings/', bookings, name='bookings'),
    path('seebookings/', seebookings, name='seebookings'),
    path('cancellings/', cancellings, name='cancellings'),
    path('admin/', admin.site.urls),
]
