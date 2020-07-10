from django.urls import path
from django.contrib import admin
from . import views
checkout=views.Checkout()
editProfile=views.EditProfile()
urlpatterns=[
    path('admin/',admin.site.urls),
    path('',views.myuserhome),
    path('cngpswd/',views.cngpswd),
    path('edit_info/',editProfile.displayInfo),
    path('save_info/', editProfile.saveInfo),
    path('getOtp/',editProfile.getOtp),
    path('resendOtp/',editProfile.resendOtp),
    path('checkOtp/',editProfile.checkOtp),
    path('viewsubcat/',views.viewsubcat),
    path('viewfood/',views.viewfood),
    path('logout/',views.logout),
    path('cart/',views.cart),
    path('display/',checkout.display),
    path('checkout/',checkout.checkout),
    path('orderlist/',views.orderList),
    path('orderDetails/',views.orderDetails),
    path('lounchfeedback/', views.lounchFeedback),
    path('trackorder/', views.trackOrder),
    path('help/', views.help),

]


