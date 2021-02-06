from __future__ import unicode_literals
from django.shortcuts import render,redirect
from collections import defaultdict
from GroceryShop import settings
from django.http.response import JsonResponse
from django.core.mail import send_mail

from .import models
import random


from datetime import datetime

curl = settings.CURRENT_URL

def home(request):
    if 'email' in request.COOKIES :
        return redirect('http://localhost:8000/groceryUser/')
    else:
        return render(request, 'home.html')

def about(request):
    if 'email' in request.COOKIES :
        return redirect('http://localhost:8000/groceryUser/about')
    else:
        return render(request, 'about.html')

def contact(request):
    if 'email' in request.COOKIES :
        return redirect('http://localhost:8000/groceryUser/contact')
    else:
        return render(request, 'contact.html')

def login(request):
    if request.method=="GET":
        return render(request, 'login.html')
    else:
        email = request.POST.get('uname')
        password = request.POST.get('psw')
        query = "select userId from customers where email ='%s' and password = '%s' "%(email,password)
        models.cursor.execute(query)
        userID =  models.cursor.fetchall()
        if userID:
            response = redirect('http://localhost:8000/groceryUser/')
            response.set_cookie('email',email)
            print("Login Done")
            return response 
        else:
            print("Login generate Error")
            return render(request,'register.html',{'output':'User Not Exist'})

def sendOtp(email,subject):
    try:
        otp = random.randint(1000, 9999)
        # msg = """ Please use this Otp for register in Grocery\nOTP : """ \
        #     + str(otp) + """\n Don't shear this Otp with anyone"""
        # to = email
        # send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
        return otp
    except:
        return  0

class Register:
    def __init__(self):
        self.user = dict()
    def register(self,request):
        if request.method=="GET":
            return render(request, 'register.html',{})
        else:
            now = datetime.now()
            self.user['registerTime'] = now.strftime("%d/%m/%Y %H:%M:%S")
            self.user['name'] = request.POST.get("name")
            self.user['email'] = self.email = username = request.POST.get("uname")
            self.user['password'] = request.POST.get("psw")
            self.user['city'] = request.POST.get("city")
            self.user['contact_no'] = request.POST.get("contact_no")
            self.user['address'] = request.POST.get("address")
            self.user['userId'] = username.split('@')[0]
            
            self.otp = sendOtp(self.email,"Mail for Registration")

            if self.otp :
                response=redirect('http://localhost:8000/checkOtp/')
                response.set_cookie("email",self.email)
                return response
            else:
                return render(request, 'register.html',{})

    def resendOtp(self,request):
        self.otp = sendOtp(self.email,"Mail for Registration")
        otpStatus = 0
        if self.otp:
            otpStatus = 1
        return JsonResponse({'otp':otpStatus})

    def checkOtp(self,request):
        if request.method=="GET":
            return render(request,'checkOtp.html',{'email':self.email})
        else:
            userOtp =  request.POST.get('userOtp')
            if int(userOtp)!=self.otp:
                return render(request,'checkOtp.html',{})
            else:
                # query = "insert into customers (userId,name,email,contact_no,city, password,address,registerDate) values('%s','%s','%s','%s','%s','%s','%s','%s')"%(self.user['userId'],self.user['name'],self.user['username'],self.user['contact_no'],self.user['city'],self.user['password'],self.user['address'],self.user['registerTime'])   
                # models.cursor.execute(query)
                # models.db.commit()
                return redirect('http://localhost:8000/login/')            
    def alreadyReg(self,request):
        username = request.POST.get('username')
        query = "select * from customers where email = '%s' "%(username)
        models.cursor.execute(query)
        userData = models.cursor.fetchall()
        if userData :
            return JsonResponse({'isRegistered':1})
        else:
            return JsonResponse({'isRegistered':0})
    # ................................
    # ................................
def temp(request):
    otp = sendOtp('akaushal451@gmail.com',"For temporary Use")
    print("OTP : ",otp)
    return render(request,'temp.html',{'otp':otp})

def product(request):
    query= 'select * from catagory'
    models.cursor.execute(query)
    item=models.cursor.fetchall()
    print(item)
    queryForCatagory = "select * from catagory"
    models.cursor.execute(queryForCatagory)
    catagoryData = models.cursor.fetchall()

    queryForItems = "select * from variety order by catId"
    models.cursor.execute(queryForItems)
    varietyData = [list(i) for i in models.cursor.fetchall()]
    varietyData = list(varietyData)
    globalData = [
    ]
    tempDict= defaultdict(list)
    for i in varietyData:
        try:
            if tempDict[i[1]]:
                temp = list(i)
                temp[5] ='image/'+temp[5]
                tempDict[i[1]].append(temp)
        except:
            temp = list(i)
            temp[5] ='image/'+temp[5]
            tempDict[i[1]] = [temp,]
    for i in range(len(catagoryData)):
        globalData.append([catagoryData[i][1],'image/'+catagoryData[i][2],catagoryData[i][3],tempDict[catagoryData[i][0]]])
    return render(request, 'product.html')
    # return render('',{'catagories':globalData})




