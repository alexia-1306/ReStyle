"""
URL configuration for ReStyle_DjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.shortcuts import render #trimite html
from django.contrib import admin #importa panoul admin django
from django.urls import path, include #path = definire rute, include = includem urls

from products.views import add_product


# from django.http import HttpResponse #afisare text direct in browser

def home(request):
    return render(request, 'home.html')
urlpatterns = [
    path('admin/', admin.site.urls),
    path("users/", include("users.urls")),
    path("", home, name='home') ,#leaga ruta de functia home
    path('', include('products.urls')),

]
