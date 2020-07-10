
from typing import re

from django.shortcuts import render,redirect
from pyparsing import unicode_set

from myapp.settings import BASE_DIR
from . import models
from django.conf import settings
from os import remove,chdir
from django.core.mail import send_mail
import random
import time
from django.core.files.storage import FileSystemStorage
from django.http.response import JsonResponse
from collections import Counter

curl=settings.CURRENT_URL
murl=settings.MEDIA_URL
def myadminhome(request):
    if 'adminMail' in request.COOKIES:
        currentOrderQuery="select * from currentorder"
        models.cursor.execute(currentOrderQuery)
        currentOrders=list(map(list,models.cursor.fetchall()))
        print(currentOrders)
        if currentOrders:
            for i in range(len(currentOrders)):
                t = currentOrders[i][4].split()
                t[3], t[1] = t[1], t[3]
                if int(t[1][:2]) >= 12:
                    hour = int(t[1][:2]) % 12
                    t[1] = str(hour) + t[1][2:5] + " PM"
                else:
                    t[1] = t[1][:5] + " AM"
                currentOrders[i][4] = t
            for i in range(len(currentOrders)):
                for j in range(len(currentOrders)):
                    if currentOrders[i][2]<currentOrders[j][2]:
                            currentOrders[i],currentOrders[j]=currentOrders[j],currentOrders[i]
            print(currentOrders)
            for i in range(len(currentOrders)):
                currentOrders[i].insert(0, i + 1)
            return render(request,"myadminhome.html",{'curl':curl,'currentOrders':currentOrders,'noOfOrder':1})
        else:
            return render(request,"myadminhome.html",{'curl':curl,'currentOrders':currentOrders,'noOfOrder':0})
    else:
        return redirect(curl+'')

def confirmOrder(request):
    orderId=request.POST.get('orderId')
    query = "UPDATE currentorder SET  status = '%d',statusMsg='%s' WHERE  orderId  = '%s' " % (2,"ORDER IS BEING PREPARED",orderId)
    models.cursor.execute(query)
    models.db.commit()
    return JsonResponse({'op':"Done"})

def assignDeliveryBoy(request):
    orderId=request.POST.get('orderId')
    userId=request.POST.get('userId')
    dpQuery="select dpId from deliverypartner WHERE status = '%d' "%(1)
    models.cursor.execute(dpQuery)
    activeDp=list(map(list,models.cursor.fetchall()))
    for i in range(len(activeDp)):
        activeDp[i]=activeDp[i][0]

    currentDp="select dpId from currentdpstatus"
    models.cursor.execute(currentDp)
    currentDp=list(map(list,models.cursor.fetchall()))
    for i in range(len(currentDp)):
        currentDp[i]=currentDp[i][0]

    availableDp=[]
    for dp in activeDp:
        if dp not in currentDp:
            availableDp.append(dp)

    if len(availableDp)>0:
        availableDp=availableDp[0]
        print("Available : ",availableDp)
        query = "UPDATE orders SET  deliveryPartnerId = '%s' WHERE orderId  = '%s' " % (availableDp,orderId)
        models.cursor.execute(query)
        models.db.commit()

        currentOrderQuery = "UPDATE currentorder SET  status = '%d',statusMsg='%s' WHERE  orderId  = '%s' " % (3, "ORDER IS BEING PREPARED", orderId)
        models.cursor.execute(currentOrderQuery)
        models.db.commit()

        query = "insert into currentdpstatus values('%s','%s','%s','%d')" % (availableDp,userId,orderId,0)
        models.cursor.execute(query)
        models.db.commit()

        return JsonResponse({'op':"1"})
    else:
        return JsonResponse({'op':'0'})

def cancelOrder(request):
    orderId=request.POST.get('orderId')
    cancelOrderQuery = "DELETE FROM currentorder WHERE orderId = '%s' " % (orderId)
    models.cursor.execute(cancelOrderQuery)
    models.db.commit()

    query = "UPDATE orders SET  orderStatus = '%d' WHERE  orderId  = '%s' " % (0,orderId)
    models.cursor.execute(query)
    models.db.commit()

    return JsonResponse({'op':"Done"})


def addcat(request):
    if 'adminMail' in request.COOKIES:
        query1="select * from catagory"
        models.cursor.execute(query1)
        clist=models.cursor.fetchall()
        if request.method=="GET":
            return render(request,"addcat.html",{'curl':curl,"output":'',"clist":clist})
        else:
            catnm=request.POST.get('catnm')
            caticon=request.FILES['caticon']
            catid=''+catnm[:3]+catnm[-1:-4:-1]+str(sum(map(ord,catnm))%1000)
            fs=FileSystemStorage()
            filename=fs.save(caticon.name,caticon)
            query="insert into catagory values('%s','%s','%s')" %(catid,catnm,filename)
            models.cursor.execute(query)
            models.db.commit()
            query2 = "select * from catagory"
            models.cursor.execute(query2)
            clist = models.cursor.fetchall()
            return render(request,"addcat.html",{"curl":curl,"output":"Catagory added successfully  ....","clist":clist})
    else:
        return redirect(curl)

def addsubcat(request):
    if 'adminMail' in request.COOKIES:
        query1 = "select * from catagory"
        models.cursor.execute(query1)
        clist = models.cursor.fetchall()
        if request.method=='GET':
            return render(request,"addsubcat.html",{'curl':curl,'clist':clist})
        else:
            subcatnm=request.POST.get('subcatnm')
            catnm=request.POST.get('catnm')
            subcaticon=request.FILES['subcaticon']
            subcatid=''+subcatnm[:3]+subcatnm[-1:-4:-1]+str(sum(map(ord,subcatnm))%1000)
            fs=FileSystemStorage()
            filename=fs.save(subcaticon.name,subcaticon)
            query="insert into subcatagory values('%s','%s','%s','%s')" %(subcatid,catnm,subcatnm,filename)
            models.cursor.execute(query)
            models.db.commit()
            return render(request,"addsubcat.html",{"curl":curl,"output":"Sub Catagory added successfully  ....","clist":clist})
    else:
        return redirect(curl)


class AddDish:
    def changeSubCat(self,request):
        if 'adminMail' in request.COOKIES:
            catagory=request.POST.get('catnm')
            subCatQuery = "select subcatnm from subcatagory WHERE catnm='%s'"%(catagory)
            models.cursor.execute(subCatQuery)
            subcatlist = models.cursor.fetchall()
            return JsonResponse({"subcatlist":subcatlist})
        else:
            return redirect(curl)
    def adddish(self,request):
        if 'adminMail' in request.COOKIES:
            query1 = "select catnm from catagory"
            models.cursor.execute(query1)
            clist = models.cursor.fetchall()
            if request.method=='GET':
                return render(request,"adddish.html",{'curl':curl,'clist':clist})
            else:
                catnm=request.POST.get('catnm')
                subcatnm=request.POST.get('subcatnm')
                dishnm=request.POST.get('dishnm')
                discription=request.POST.get('discription')
                price=float(request.POST.get('price'))
                query="insert into food values(NULL,'%s','%s','%s','%f','%s')" %(catnm,subcatnm,dishnm,price,discription)
                models.cursor.execute(query)
                models.db.commit()
                return render(request,"adddish.html",{"curl":curl,'clist':clist,"output":"Sub Catagory added successfully  ...."})
        else:
            return redirect(curl)

class ManageDish:
    def changeFood(self,request):
        if 'adminMail' in request.COOKIES:

            catagory = request.POST.get('catnm')
            subCatagory = request.POST.get('subcatnm')
            dishQuery = "select dish from food WHERE catagory='%s' and subcatagory='%s'" % (catagory,subCatagory)
            models.cursor.execute(dishQuery)
            dishlist = models.cursor.fetchall()
            return JsonResponse({'dishlist':dishlist})
        else:
            return redirect(curl)
    def managedish(self,request):
        if 'adminMail' in request.COOKIES:
            query1 = "select catnm from catagory"
            models.cursor.execute(query1)
            clist = models.cursor.fetchall()
            if request.method=='GET':
                return render(request,'managedish.html',{'clist':clist,'curl':curl})
            else:
                catagory = request.POST.get('catnm')
                subCatagory = request.POST.get('subcatnm')
                dish = request.POST.get('dish')
                removeDishQuery = "DELETE FROM food WHERE catagory='%s' and subcatagory='%s' and dish='%s' " % (catagory,subCatagory,dish)
                models.cursor.execute(removeDishQuery)
                models.db.commit()
                return render(request,'managedish.html',{'clist':clist,'curl':curl})
        else:
            return redirect(curl)

def managecat(request):
    if 'adminMail' in request.COOKIES:

        query1="select * from catagory"
        models.cursor.execute(query1)
        clist=models.cursor.fetchall()
        if request.method=='GET':
            return render(request,"managecat.html",{'curl':curl,"output":'','clist':clist})
        else:
            catnm=request.POST.get('catnm')
            query4="select * from catagory WHERE catnm = '%s' "%(catnm)
            models.cursor.execute(query4)
            cat=models.cursor.fetchall()
            caticon=cat[0][2]
            query2="DELETE FROM catagory WHERE catnm = '%s' "%(catnm)
            models.cursor.execute(query2)
            models.db.commit()
            try:
                chdir("media")
                remove(caticon)
                chdir("..")
            except:
                print("File is not placed on the location")
            query3 = "select * from catagory"
            models.cursor.execute(query3)
            clist = models.cursor.fetchall()
            return render(request,"managecat.html",{'curl':curl,"output":catnm+' Deleted....','clist':clist})
    else:
        return redirect(curl)

def managesubcat(request):
    if 'adminMail' in request.COOKIES:

        query1="select catnm from catagory"
        models.cursor.execute(query1)
        clist=models.cursor.fetchall()
        if request.method=='GET':
            return render(request,"managesubcat.html",{'curl':curl,"output":'','clist':clist})
        else:
            catnm=request.POST.get('catnm')
            subcatnm=request.POST.get('subcatnm')
            query3="select * from subcatagory WHERE catnm = '%s' and subcatnm = '%s' "%(catnm,subcatnm)
            models.cursor.execute(query3)
            subcat=models.cursor.fetchall()
            subcaticon=subcat[0][3]
            query4="DELETE FROM subcatagory WHERE catnm = '%s' and subcatnm = '%s' "%(catnm,subcatnm)
            models.cursor.execute(query4)
            models.db.commit()
            try:
                chdir("media")
                remove(subcaticon)
                chdir("..")
            except:
                print("File is not placed on the location")
            return render(request,"managesubcat.html",{'curl':curl,"output":subcatnm+' Deleted....','clist':clist})
    else:
        return redirect(curl)

def lounch_notf(request):
    if 'adminMail' in request.COOKIES:
        if request.method=="GET":

            query = "select * from notification"
            models.cursor.execute(query)
            notifications = models.cursor.fetchall()
            return render(request,"lounch_notf.html",{"curl":curl,"output":'','notifications':notifications})
        else :
            notification=request.POST.get('notf')
            print(notification)
            query="insert into notification values(NULL,'%s')" %(notification)
            models.cursor.execute(query)
            models.db.commit()

            query = "select * from notification"
            models.cursor.execute(query)
            notifications = models.cursor.fetchall()

            return render(request,"lounch_notf.html",{'curl':curl,"output":"Notification Lounched....",'notifications':notifications})
    else:
        return redirect(curl)

def deleteNotf(request):
    notfId=request.POST.get('notfId')
    query="DELETE from notification WHERE notf_no = '%d' "%(int(notfId))
    models.cursor.execute(query)
    models.db.commit()
    return JsonResponse({'op':1})

def orderDetails(request):
    if 'adminMail' in request.COOKIES:

        query="select orderId,userId,orderStatus,deliveryPartnerId from orders ORDER BY orderId DESC"
        models.cursor.execute(query)
        orders=models.cursor.fetchall()
        orders=list(orders)
        for i in range(len(orders)):
            orders[i]=list(orders[i])
            orders[i].insert(0,i+1)
        return render(request,"orderdetails.html",{'curl':curl,'orders':orders})
    else:
        return redirect(curl)

def orderIdDetail(request):
    if 'adminMail' in request.COOKIES:
        orderId = request.POST.get('oId')
        userId = request.POST.get('uId')
        deliveryPartnerId = request.POST.get('dId')
        userQuery="select name,email,mobile,gender from  registration WHERE  userId = '%s' "%(userId)
        models.cursor.execute(userQuery)
        userInfo=list(models.cursor.fetchall()[0])
        orderQuery="select * from orders where orderId= '%s' "%(orderId)
        models.cursor.execute(orderQuery)
        orderInfo=list(models.cursor.fetchall()[0])
        return JsonResponse({'userInfo':userInfo,'orderInfo':orderInfo})
    else:
        return redirect(curl)


def paymentHistory(request):
    paymentHistQuery="select * from payment ORDER BY orderId DESC"
    models.cursor.execute(paymentHistQuery)
    paymentHistory=list(map(list,models.cursor.fetchall()))
    for i in range(len(paymentHistory)):
        paymentHistory[i].insert(0,i+1)
    print(paymentHistory)
    return render(request,"trxnhistory.html",{'curl':curl,'paymentHistory':paymentHistory})

class UserDetail:

    def sendOtp(self):
        self.otp = random.randint(1000, 9999)
        subject = "Register On Book My Meal"
        msg = """ Please use this Otp for register in Book My Meal\nOTP : """ \
              + str(self.otp) + """\n Don't shear this Otp with anyone"""
        to = self.email
        send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])


    def userDetails(self,request):

        if 'adminMail' in request.COOKIES:

            userDetailsQuery="select userId,name,email,mobile,gender,address,city,status,dt from registration"
            models.cursor.execute(userDetailsQuery)
            userDetails=models.cursor.fetchall()
            userDetails = list(userDetails)
            for i in range(len(userDetails)):
                userDetails[i] = list(userDetails[i])
                userDetails[i].insert(0, i + 1)
                if userDetails[i][8] ==1:
                    userDetails[i][8]="Active"
                else:
                    userDetails[i][8]="Blocked"
            return render(request,"userdetails.html",{'curl':curl,'users':userDetails})
        else:
            return redirect(curl)

    def getOtp(self,request):
        if 'adminMail' in request.COOKIES:

            models.cursor.execute("select * from registration where email='%s' "%(request.POST.get('email')))
            email = models.cursor.fetchall()
            if email :
                return JsonResponse({'otp': 0})
            else:
                self.email=request.POST.get('email')
                self.sendOtp()
                return JsonResponse({'otp':1})
        else:
            return redirect(curl)

    def checkOtp(self,request):
        if 'adminMail' in request.COOKIES:
            userOtp=request.POST.get('otp')
            userId=request.POST.get('id')
            if userOtp == str(self.otp):
                query = "UPDATE registration SET  email = '%s' WHERE  userId  = '%s' " % (self.email,userId)
                models.cursor.execute(query)
                models.db.commit()
                return JsonResponse({'otp':1})
            else:
                return JsonResponse({'otps':0})
        else:
            return redirect(curl)

    def resendOtp(self,request):
        if 'adminMail' in request.COOKIES:
            self.sendOtp()
            return JsonResponse({'otp':1})
        else:
            return redirect(curl)

    def saveInfo(self,request):
        if 'adminMail' in request.COOKIES:
            userId=request.POST.get('userId')
            status=request.POST.get('status')
            if status=="Active":
                status=1
            else:
                status=0
            email=request.POST.get('email')
            mobile=request.POST.get('mobile')
            query = "UPDATE registration SET  email = '%s',mobile='%s',status='%d' WHERE  userId  = '%s' " % (email,mobile,status,userId)
            models.cursor.execute(query)
            models.db.commit()
            return redirect(curl+"myadmin/userdetails")
        else:
            return redirect(curl)

    def deleteUser(self,request):

        if 'adminMail' in request.COOKIES:

            userId=request.POST.get('id')
            query="DELETE from registration where userId= '%s' "%(userId)
            models.cursor.execute(query)
            models.db.commit()
            return JsonResponse({'op':1})

        else:
            return redirect(curl)

def viewFeedback(request):
    if 'adminMail' in request.COOKIES:
        rateQuery="select rate from ratting"
        models.cursor.execute(rateQuery)
        ratting=list(map(list,models.cursor.fetchall()))

        feedbackQuery="select feedback from ratting"
        models.cursor.execute(feedbackQuery)
        feedback = list(map(list, models.cursor.fetchall()))
        temp=[]
        for i in feedback:
            if len(i[0]) > 1:
                temp.append(i[0])
        feedback=temp
        for i in range(len(ratting)):
            ratting[i]=int(round(ratting[i][0]))

        ratting=dict(Counter(ratting))
        ratting['total']=sum(ratting.values())
        ratting=[ratting['total'],ratting[1],ratting[2],ratting[3],ratting[4],ratting[5],]
        return render(request,"viewfeedback.html",{'curl':curl,'ratting':ratting,'feedback':feedback})
    else:
        return redirect(curl)

class AddDeliveryPartner:
    def sendOtp(self):
        self.otp = random.randint(1000, 9999)
        # subject = "Register On Book My Meal"
        # msg = """ Please use this Otp for register in Book My Meal\nOTP : """ \
        #       + str(self.otp) + """\n Don't shear this Otp with anyone"""
        # to = self.dpEmail
        # send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])

    def resendOtp(self, request):
        print("REsend Otp Called")
        self.sendOtp()
        print("OTp : ", self.otp)
        return JsonResponse({'otp': 1})

    def dpValidOtp(self,request):
        otp=request.POST.get('otp')
        if self.otp==int(otp):
            print(self.dpEmail,self.dpName,self.dpAddress,self.dpId)
            query = "insert into deliverypartner values('%s','%s','%s','%s','%s','%s','%s','%s','%d')" % (self.dpId,self.dpName.title(),self.dpEmail,"dpbmm@1234",self.dpMobile,self.dpGender,self.dpAddress,time.asctime(time.localtime(time.time())),0)
            models.cursor.execute(query)
            models.db.commit()
            return JsonResponse({'otp':1})
        else:
            return JsonResponse({'otp':0})


    def addDeliveryPartner(self,request):
        self.dpName=request.POST.get('dpname')
        self.dpEmail=request.POST.get('dpemail')
        self.dpMobile=request.POST.get('dpmobile')
        self.dpGender=request.POST.get('dpgender')
        self.dpAddress=request.POST.get('dpaddress')
        print(request.POST)
        self.dpId="DP"+str(sum(map(ord, self.dpEmail)) % 1000)+list(map(str, self.dpEmail.split("@")))[0]

        self.sendOtp()
        print("OTP : ",self.otp)
        return render(request,"dpvalidotp.html",{"email":self.dpEmail})


def logout(request):
    if 'adminMail' in request.COOKIES:
        response=redirect(curl+'')
        response.delete_cookie('adminMail')
        return response
    else:
        return redirect(curl + '')
