from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.http.response import JsonResponse
from . import models
import json
from datetime import datetime
currentOrder = 0
def home(request):
    if 'email' in request.COOKIES :
        query = "select * from currentorders where userId = '%s' " % (request.COOKIES['email'].split('@')[0])
        models.cursor.execute(query)
        currentOrder = models.cursor.fetchall()
        if currentOrder:
            currentOrder = 1
        else:
            currentOrder = 0
        return render(request,'userBase.html',{'currentOrder':currentOrder})
    else:
        return redirect("http://localhost:8000/")

def about(request):
    query = "select * from currentorders where userId = '%s' " % (request.COOKIES['email'].split('@')[0])
    models.cursor.execute(query)
    currentOrder = models.cursor.fetchall()
    if currentOrder:
        currentOrder = 1
    else:
        currentOrder = 0
    if 'email' in request.COOKIES :
        return render(request,'AboutUs.html',{'currentOrder':currentOrder})
    else:
        return redirect("http://localhost:8000/")

def contact(request):
    return render(request,'contact.html',{})

def product(request):
    query = "select * from subvariety"
    models.cursor.execute(query)
    subvarietyData = models.cursor.fetchall()
    return render(request,'userSubVariety.html',{'items':subvarietyData,'currentOrder':currentOrder})

def cart(request):
    if request.method=="GET":
        return render(request,'cart.html',{'currentOrder':currentOrder})
    else:
        orderItems=json.loads(request.POST.get('groceryItems'))
        print(type(orderItems))
        print(orderItems)
        address=request.POST.get('address')
        deliveryNote=request.POST.get('deliveryNote')
        cartNumber=request.POST.get('cartNumber')
        query = "select count(orderId) from orders";
        models.cursor.execute(query)
        orderId = 'ORD000'+str(models.cursor.fetchall()[0][0]+1)
        userId = request.COOKIES['email'].split('@')[0]
        print("CArt : ",userId)
        now = datetime.now()
        orderTime =now.strftime("%d/%m/%Y %H:%M:%S")
        query = "insert into orders (orderId,userId,orderTime,deliveryNote,address,orderItems) values('%s','%s','%s','%s','%s','%s')"%(orderId,userId,orderTime,deliveryNote,address,orderItems)
        models.cursor.execute(query)
        models.db.commit()
        
        query = "insert into currentorders (orderId,userId) values('%s','%s')"%(orderId,userId)
        models.cursor.execute(query)
        models.db.commit()

        return JsonResponse({'output':1})
def AboutUs(request):
    return render(request,'AboutUs.html',{'currentOrder':currentOrder})

def ContactUs(request):
    return render(request,'ContactUs.html',{'currentOrder':currentOrder})



def logout(request):
   if 'email' in request.COOKIES:
       response = redirect('http://localhost:8000/')
       response.delete_cookie('email')
       return response
   else:
       return redirect('http://localhost:8000/')

def trackOrder(request):
    query="select * from currentorders where userId='%s' "%(request.COOKIES['email'].split('@')[0].lower())
    models.cursor.execute(query)
    currentOrderData=models.cursor.fetchall()[0]
    print(currentOrderData)
    status=currentOrderData[2]
    orderId=currentOrderData[0]
    print("status : ",status)
    return render(request,'trackorder.html',{'status':status,'orderId':orderId})