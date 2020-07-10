from django.urls import path
from django.contrib import admin
from . import views
home=views.DpHome()
editProfile=views.EditProfile()
urlpatterns=[
    path('admin/',admin.site.urls),
    path('',home.dpHome),
    path('acceptOrder/',home.acceptOrder),
    path('cancelOrder/',home.cancelOrder),
    path('pickUpOrder/',home.pickUpOrder),
    path('deliveredOrder/',home.deliveredOrder),
    path('changeStatus/',views.changeStatus),
    path('editProfile/',editProfile.displayInfo),
    path('getOtp/',editProfile.getOtp),
    path('resendOtp/',editProfile.resendOtp),
    path('checkOtp/', editProfile.checkOtp),
    path('save_info/', editProfile.saveInfo),
    path('previousOrders/', views.previousOrders),
    path('logout/',views.logout),

]