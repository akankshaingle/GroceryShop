from  django.shortcuts  import render,redirect
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from requests import request

from . import models
from django.http.response import JsonResponse

import time
import random
from email.mime.text import MIMEText
import os
curl=settings.CURRENT_URL
media_url=settings.MEDIA_URL

foodQuery = "select * from food"
models.cursor.execute(foodQuery)
globalFoodData = models.cursor.fetchall()

notfQuery="select notf_data from notification"
models.cursor.execute(notfQuery)
notifications=models.cursor.fetchall()
os.path.abspath(os.path.dirname(__name__))

def home(request):
    if 'email' in request.COOKIES :
        return redirect(curl+'myuser/')
    elif 'adminMail' in request.COOKIES:
        return redirect(curl + 'myadmin/')
    elif 'dpId' in request.COOKIES:
        return redirect(curl + 'dp/')
    else:
        query = "select * from catagory"
        models.cursor.execute(query)
        clist = models.cursor.fetchall()
        response=render(request, "home.html",{'curl': curl, 'notifications': notifications, 'clist': clist, 'media_url': media_url,'quickMenuFood': globalFoodData})
        return response

def quickSearchBar(request):
    if "myuser" in request.POST.get("currentURL"):
        url=curl+"myuser/viewfood/?subcatid="
    else:
        url=curl+"viewfood/?subcatid="
    subcatQuery = "select subcatid,catnm,subcatnm from subcatagory"
    models.cursor.execute(subcatQuery)
    subcatList = models.cursor.fetchall()

    foodQuery = "select catagory,subcatagory,dish from food"
    models.cursor.execute(foodQuery)
    foodList = models.cursor.fetchall()
    foodData=list()

    for subcat in subcatList:
        for food in foodList:
            if subcat[1]==food[0] and subcat[2]==food[1]:
                foodData.append({'label':food[2],'value':url+subcat[0]})
    return JsonResponse({'foodData':foodData})

def viewsubcat(request):
    catid=request.GET.get('catid')
    query = "select * from catagory where catid='%s'"%(catid)
    models.cursor.execute(query)
    clist = models.cursor.fetchall()[0]
    query1 = "select * from subcatagory WHERE catnm = '%s' "%(clist[1])
    models.cursor.execute(query1)
    subcatlist = models.cursor.fetchall()

    if len(subcatlist)>1:
        return render(request,"viewsubcat.html",{'curl':curl,'notifications':notifications,'quickMenuFood':globalFoodData,'clist':clist,'subcatlist':subcatlist,'catnm':clist[1],'media_url':media_url})
    else:
        return redirect(curl + "viewfood/?subcatid=" + subcatlist[0][0])

def viewfood(request):
    subcatid = request.GET.get('subcatid')
    query1="select catnm,subcatnm from subcatagory WHERE subcatid= '%s' "%(subcatid)
    models.cursor.execute(query1)
    dishDetail=list(models.cursor.fetchall()[0])
    catQuery = "select catid from catagory where catnm='%s' " % (dishDetail[0])
    models.cursor.execute(catQuery)
    catid = models.cursor.fetchall()[0][0]
    dishDetail.append(catid)
    if 'email' in request.COOKIES:
        return redirect(curl+"myuser/viewfood")
    else:
        query="select * from food where catagory = '%s' and subcatagory = '%s' "%(dishDetail[0],dishDetail[1])
        models.cursor.execute(query)
        foodlist = models.cursor.fetchall()
        return render(request,"viewfood.html",{'curl':curl,'notifications':notifications,'quickMenuFood':globalFoodData,'foodlist':foodlist,'dishMetaData':dishDetail})

def contact(request):
    return render(request,"contact.html",{'curl':curl,'notifications':notifications,'quickMenuFood':globalFoodData})

def about(request):
    return render(request,"about.html",{'curl':curl,'notifications':notifications,'quickMenuFood':globalFoodData})
class Register:
    def __init__(self):
        self.email=''
    def sendOtp(self):
        self.otp = random.randint(1000, 9999)
        subject = "Register On Book My Meal"
        msg = """ Please use this Otp for register in Book My Meal\nOTP : """ \
              + str(self.otp) + """\n Don't shear this Otp with anyone"""
        to = self.email
        send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])

    def authOtp(self,request):
        if request.method=='POST':
            self.name = request.POST.get('name');
            self.email = request.POST.get('email');
            self.mobile = request.POST.get('mobile');
            self.gender = request.POST.get('gender');
            self.address = request.POST.get('address');
            self.city = request.POST.get('city');
            self.password = request.POST.get('password');
            self.status = request.POST.get('status');
            self.role = request.POST.get('role');
            self.dt = time.asctime(time.localtime(time.time()))
            self.sendOtp()
            print("Runninfn Auth Otp")
            response=render(request, "register_validOtp.html", {"curl": curl,'notifications':notifications,'quickMenuFood':globalFoodData, "output": 'Otp sent successfully...','email':self.email})
            response.set_cookie("registerMail", self.email)
            return response
        else:
            response=render(request, "register_validOtp.html", {"curl": curl,'notifications':notifications,'quickMenuFood':globalFoodData, "output": 'Otp sent successfully...','email':self.email})
            response.set_cookie("registerMail", self.email)
            return response



    def validOtp(self,request):
        if 'registerMail' in request.COOKIES:
            otp = int(request.POST.get('otp'))
            if otp==self.otp:
                list(map(int,))
                [username,temp]=list(map(str,self.email.split("@")))
                query = "insert into registration values('%s','%s','%s','%s','%s','%s','%s','%s','user',0,'%s')" % (
                username.title(),self.name.title(), self.email.lower(), self.password, self.address.title(), self.mobile, self.city.title(), self.gender.title(), self.dt)
                models.cursor.execute(query)
                models.db.commit()
                del request.COOKIES['registerMail']
                return JsonResponse({'otp':1})
            else:
                return JsonResponse({'otp':0})
        else:
            return redirect(curl)

    def changeMail(self,request):
        query="select email from registration where email='%s'"%(''+request.POST.get('email').lower())
        models.cursor.execute(query)
        email = models.cursor.fetchall()
        if email :
            return JsonResponse({'otp':0})
        else:
            self.email=request.POST.get('email')
            self.sendOtp()
            response = JsonResponse({'email':self.email,'otp':1})
            response.set_cookie('registerMail',self.email)
            return response

    def resendOtp(self,request):
        self.sendOtp()
        return JsonResponse({'otp':1})

def userLogin(request):
    email=request.POST.get('loginEmail')
    password = request.POST.get('loginPassword')
    query="select * from registration where email='%s' and password='%s' "%(email,password)
    models.cursor.execute(query)
    user=models.cursor.fetchall()
    if len(user)>0:
        if user[0][8]=='user':
            response=redirect(curl+"myuser/")
            response.set_cookie("email",email)
            return response
        else:
            response = redirect(curl+"myadmin/")
            response.set_cookie("adminMail",email)
            return response
    else:
        return redirect(curl)


def dpLogin(request):
    email=request.POST.get('dploginEmail')
    password = request.POST.get('dploginPassword')
    query="select dpId from deliverypartner where dpEmail='%s' and dpPassword='%s' "%(email,password)
    models.cursor.execute(query)
    dpExist=models.cursor.fetchall()
    if len(dpExist)>0:
        response=redirect(curl+"dp/")
        response.set_cookie("dpId",dpExist[0][0])
        return response
    else:
        return redirect(curl)


class Valid:
    def __init__(self):
        self.email=''
    def sendOtp(self):
        self.otp = random.randint(1000, 9999)
        subject = "Re-set Password"
        msg = """<html>
        
                        <head></head>
                        <body>
                            <h1>Welcome to Book My Meal</h1>
                            <p>Please use this OTP to reset your Password</p>
                            <h2> OTP : """ + str(self.otp) + """</h2>
                            <br>
                        </body>
                    </html>"""
        to = self.email
        send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])

    def forgotPassword(self,request):
        if request.method=='GET':
            if "email" in request.COOKIES:
                response=render(request,"forgotPassword.html",{'curl':curl,'notifications':notifications,'quickMenuFood':globalFoodData,'otp':0})
                response.delete_cookie('email')
                return response
            else:
                return render(request,"forgotPassword.html",{'curl':curl,'notifications':notifications,'quickMenuFood':globalFoodData})

        else:
            self.email = request.POST.get('email')
            query1="select * from registration WHERE email = '%s' "%(self.email)
            models.cursor.execute(query1)
            ulist=models.cursor.fetchall()
            if len(ulist) > 0:
                self.sendOtp()
                return JsonResponse({"otp":1,'email':self.email})
            else:
                output="Please Enter the Email Assosiated with BookMyMeal Account"
                return JsonResponse({"otp":0})

    def verifyotp(self,request):
        if self.email:
            if request.method == 'GET':
                return render(request,"forgotPassword.html",{'curl':curl,'notifications':notifications,'quickMenuFood':globalFoodData,'output':'','email':self.email})
            else:
                otp = int(request.POST.get('otp'))
                if otp == self.otp:
                    return JsonResponse({'otp':1})
                else:
                    return JsonResponse({'otp':0})
        else:
            return redirect(curl)


    def resendOtp(self,request):
        if self.email:
            self.email=request.POST.get('email')
            self.sendOtp()
            return JsonResponse({'otp':1,'email':self.email})
        else:
            return redirect(curl)

    def resetPswd(self,request):
        if self.email:
            password=request.POST.get("fpNewPassword")
            email=self.email
            query="UPDATE registration SET  password =  '%s' WHERE  email = '%s' "%(password,email)
            models.cursor.execute(query)
            models.db.commit()
            subject = "Password set"
            msg = """<html>
                        <head></head>
                        <body>
                            <h1>Welcome to Book My Meal</h1>
                            <p>Your Password is changed</p>
                            <p>Your new Password is """+str(password)+"""</p>
                            <h2>Don't Shear Your otp and Password to Any other person </h2>
                            <br>
                        </body>
                    </html>"""
            to = email
            send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
        else:
            return redirect(curl)

        return redirect(curl)
def help(request):
    return render(request,"help.html",{'curl':curl,'notifications':notifications,'quickMenuFood':globalFoodData})