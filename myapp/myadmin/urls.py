from django.urls import path
from django.contrib import admin
from . import views
addDishObj=views.AddDish()
manageDishObj=views.ManageDish()
userDetail=views.UserDetail()
addDp=views.AddDeliveryPartner()
urlpatterns=[
    path('admin/',admin.site.urls),
    path('',views.myadminhome),
    path('addcat/',views.addcat),
    path('addsubcat/',views.addsubcat),
    path('adddish/',addDishObj.adddish),
    path('changeSubCat/',addDishObj.changeSubCat),
    path('managecat/',views.managecat),
    path('managesubcat/', views.managesubcat),
    path('managedish/', manageDishObj.managedish),
    path('changeFood/', manageDishObj.changeFood),
    path('lounch_notf/',views.lounch_notf),
    path('deleteNotf/',views.deleteNotf),
    path('orderdetails/',views.orderDetails),
    path('orderIdDetails/',views.orderIdDetail),
    path('userdetails/',userDetail.userDetails),
    path('getOtp/',userDetail.getOtp),
    path('checkOtp/', userDetail.checkOtp),
    path('resendOtp/', userDetail.resendOtp),
    path('saveInfo/', userDetail.saveInfo),
    path('deleteUser/', userDetail.deleteUser),
    path('viewFeedback/',views.viewFeedback),
    path('confirmOrder/',views.confirmOrder),
    path('assignDeliveryBoy/',views.assignDeliveryBoy),
    path('cancelOrder/',views.cancelOrder),
    path('paymentHistory/',views.paymentHistory),
    path('addDeliveryPartner/', addDp.addDeliveryPartner),
    path('dpResendOtp/', addDp.resendOtp),
    path('dpValidOtp/', addDp.dpValidOtp),
    path('logout/',views.logout),

]