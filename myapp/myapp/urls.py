"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from distutils.command.register import register
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
obj=views.Valid()
register=views.Register()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('home/',views.home),
    path('quickSearchBar/',views.quickSearchBar),
    path('viewsubcat/',views.viewsubcat),
    path('viewfood/',views.viewfood),
    path('about/',views.about),
    path('contact/',views.contact),
    path('authOtp/',register.authOtp),
    path('validOtp/',register.validOtp),
    path('changeMail/',register.changeMail),
    path('authResendOtp/',register.resendOtp),
    path('userLogin/',views.userLogin),
    path('dpLogin/',views.dpLogin),
    path('forgotPassword/',obj.forgotPassword),
    path('verifyotp/',obj.verifyotp),
    path('resendOtp/',obj.resendOtp),
    path('resetPswd/',obj.resetPswd),
    path('help/',views.help),
    path('myuser/',include('myuser.urls')),
    path('myadmin/',include('myadmin.urls')),
    path('dp/',include('deliveryPartner.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
