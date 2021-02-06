"""GroceryShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path,include
from django.contrib import admin
from . import views
adminHome = views.AdminHome()
urlpatterns = [ 
    path('',adminHome.home),
    path('adminHome', adminHome.home),
    path('confirmOrder/', adminHome.confirmOrder),
    path('prepareOrder/', adminHome.prepareOrder),
    path('doneOrder/', adminHome.doneOrder),
    path('deliveryOrder/', adminHome.deliveryOrder),
    path('deleteOrder/', adminHome.deleteOrder),
    path('addcatagory/',views.addCatagory),
    path('deletecatagory/',views.deleteCatagory),
    path('deletevariety/',views.deleteVariety),
    path('deletesubvariety/',views.deleteSubVariety),
    path('addvariety/',views.addVariety),
    path('addsubvariety/',views.addSubVariety),
    path('changecatagory/',views.changeCatagory),
    path('changevariety/',views.changeVariety),
]

