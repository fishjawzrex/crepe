"""crepe_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from crepe_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('toppings/', views.Toppings.as_view()),
    path('nuts/', views.Nuts.as_view()),
    path('fruits/', views.Fruits.as_view()),
    path('beverages/', views.Beverages.as_view()),
    path('wraps/', views.Wraps.as_view()),
    path('sides/', views.Sides.as_view()),
    path('crepes/', views.Crepes.as_view()),
    path('orders/', views.Orders.as_view()),
    path('customers/', views.Customers.as_view()),

]
