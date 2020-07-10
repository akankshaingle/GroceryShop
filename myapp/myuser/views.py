
from django.shortcuts import render,redirect

from django.http import HttpResponse
from django.conf import settings
from . import models
import random
from django.core.mail import send_mail
from django.http.response import JsonResponse
import json
import time
from django.views.decorators.csrf import csrf_exempt
from . import paytm_checksum as paytm
curl=settings.CURRENT_URL
media_url=settings.MEDIA_URL
MERCHANT_KEY="IVqLU9EC%_1szfPo"
notfQuery = "select notf_data from notification"
models.cursor.execute(notfQuery)
notifications = models.cursor.fetchall()


foodQuery = "select * from food"
models.cursor.execute(foodQuery)
globalFoodData = models.cursor.fetchall()

currentOrder=''
def myuserhome(request):
    if 'email' in request.COOKIES :
        print(request.COOKIES["email"])
        query = "select * from catagory"
        models.cursor.execute(query)
        clist = models.cursor.fetchall()
        print(clist)
        email=request.COOKIES['email']

        currentOrderQuery = "select * from currentorder where userId='%s' " % (request.COOKIES['email'].split('@')[0])
        models.cursor.execute(currentOrderQuery)
        if models.cursor.fetchall():
            currentOrder=1
        else:
            currentOrder=0
        return render(request,"myuserhome.html",{'curl':curl,'quickMenuFood':globalFoodData,'notifications':notifications,'clist':clist,'media_url':media_url,'currentOrder':currentOrder})
    else:
        return redirect(curl+'')


def cngpswd(request):
    if 'email' in request.COOKIES:
        if request.method=='GET':
            return render(request,"cngpswd.html",{'curl':curl,'quickMenuFood':globalFoodData,'notifications':notifications,'currentOrder':currentOrder})
        else:
            models.cursor.execute("select * from registration where email= '%s' and password = '%s' "%(request.COOKIES['email'],request.POST.get('currentPassword')))
            if(models.cursor.fetchall()):
                updateQuery = "UPDATE registration SET password='%s'  WHERE email='%s'" % (request.POST.get('newPassword'),request.COOKIES['email'])
                models.cursor.execute(updateQuery)
                models.db.commit()
                response = redirect(curl + '')
                response.delete_cookie('email')
                return response
            else:
                return render(request,"cngpswd.html",{'curl':curl,'notifications':notifications,'output':'Please Enter Correct Password..','currentOrder':currentOrder})
    else:
        return redirect(curl + '')

class EditProfile:
    def displayInfo(self,request):
        print("DisplayInfo has called")
        if 'email' in request.COOKIES:
            query = "select * from registration where email like '" + request.COOKIES['email'] + "'"
            models.cursor.execute(query)
            clist = models.cursor.fetchall()
            clist = clist[0]
            self.user = {"name": clist[1], "email": clist[2], "address": clist[4], "city": clist[6], "gender": clist[7],
                         "password": clist[3]}
            if request.method=='POST':
                password = request.POST.get('editProfilePassword');
                if self.user['password']==password:
                    return render(request,"edit_info.html",{'curl':curl,'quickMenuFood':globalFoodData,'notifications':notifications,'user':self.user ,'media_url':media_url,"op":"output",'currentOrder':currentOrder})
                else:
                    return redirect(curl)
            else:
                print(self.user)
                return render(request, "edit_info.html",{'curl': curl, 'quickMenuFood': globalFoodData, 'notifications': notifications,'user': self.user, 'media_url': media_url, "op": "output",'currentOrder':currentOrder})
        else:
            return redirect(curl)

    def saveInfo(self,request):
        print("SaveInfo has called")
        if request.method=='POST':
            self.user['name']=request.POST.get('editProfileName')
            self.user['address']=request.POST.get('editProfileAddress')
            self.user['city']=request.POST.get('editProfileCity')
            self.user['gender']=request.POST.get('editProfileGender')
            updateQuery="UPDATE registration SET name='%s',address='%s',city='%s',gender='%s',password='%s'  WHERE email='%s'"%(self.user['name'],self.user['address'],self.user['city'],self.user['gender'],self.user["password"],self.user['email'])
            models.cursor.execute(updateQuery)
            models.db.commit()
            print(self.user)

            return render(request,"edit_info.html",{'curl':curl,'quickMenuFood':globalFoodData,'notifications':notifications,'user':self.user ,'media_url':media_url,"op":"output",'currentOrder':currentOrder})
        else:
            return render(request,"edit_info.html",{'curl':curl,'quickMenuFood':globalFoodData,'notifications':notifications,'user':self.user ,'media_url':media_url,"op":"output",'currentOrder':currentOrder})

    def sendOtp(self):
        print("SendOtp has called")
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
        to = self.user['email']
        send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])

    def getOtp(self,request):
        print("getOtp has called")
        self.sendOtp()
        print("OTP : ",self.otp)
        self.newPassword=request.POST.get('password')
        print(self.user)
        return HttpResponse("DOne")

    def resendOtp(self,request):
        print("ResendOtp has called")
        self.sendOtp()
        print("REsend OTP :",self.otp)
        print(self.user)
        return HttpResponse("OTP Resend Successfully")

    def checkOtp(self,request):
        print("CheckOtp has called")
        otp=request.POST.get('otp')
        print(otp)
        print(self.otp)
        if int(otp)==int(self.otp):
            print("OTP is same")
            self.user["password"]=self.newPassword
            print(self.user)
            return JsonResponse({"otpValue":1,"password":self.newPassword})
        else:
            print("OTP is diffrent")
            return JsonResponse({"otpValue":0})

        print(self.user)


def viewfood(request):
    if 'email' in request.COOKIES:
        subcatid = request.GET.get('subcatid')
        subcatQuery="select catnm,subcatnm from subcatagory WHERE subcatid = '%s' "%(subcatid)
        models.cursor.execute(subcatQuery)
        dishDetail=list(models.cursor.fetchall()[0])
        print("dishDetail : ",dishDetail)
        catQuery = "select catid from catagory where catnm='%s' "%(dishDetail[0])
        models.cursor.execute(catQuery)
        catid=models.cursor.fetchall()[0][0]
        dishDetail.append(catid)
        query = "select * from food where catagory = '%s' and subcatagory = '%s' " % (dishDetail[0],dishDetail[1])
        models.cursor.execute(query)
        foodlist = models.cursor.fetchall()
        print("foodlist : ",foodlist)
        return render(request, "viewfooduser.html", {'curl': curl,'quickMenuFood':globalFoodData,'notifications':notifications, 'foodlist': foodlist,'currentOrder':currentOrder,'dishMetaData':dishDetail})
    else:
        return redirect(curl + '')

def viewsubcat(request):
    if 'email' in request.COOKIES:
        catid=request.GET.get('catid')
        query = "select * from catagory where catid= '%s' "%(catid)
        models.cursor.execute(query)
        clist = models.cursor.fetchall()[0]
        query1 = "select * from subcatagory WHERE catnm = '%s' "%(clist[1])
        models.cursor.execute(query1)
        subcatlist = models.cursor.fetchall()
        if len(subcatlist)>1:
            return render(request,"viewsubcatuser.html",{'curl':curl,'quickMenuFood':globalFoodData,'notifications':notifications,'clist':clist,'subcatlist':subcatlist,'catnm':clist[1],'media_url':media_url,'currentOrder':currentOrder})
        else:
            return redirect(curl+"myuser/viewfood/?subcatid="+subcatlist[0][0])
    else:
        return redirect(curl + '')

def help(request):
    if 'email' in request.COOKIES:
        return render(request,"userhelp.html",{'curl':curl,'quickMenuFood':globalFoodData,'notifications':notifications})
    else:
        return redirect(curl)

def logout(request):
    if 'email' in request.COOKIES:
        print("logout")
        response=redirect(curl+'')
        response.delete_cookie('email')
        return response
    else:
        return redirect(curl + '')

def cart(request):
    if 'email' in request.COOKIES:
        if request.method=='GET':
            return render(request,"cart.html",{'quickMenuFood':globalFoodData,'curl':curl,'currentOrder':currentOrder})
        else:
            return render(request,'cart.html',{'quickMenuFood':globalFoodData,'curl':curl,'currentOrder':currentOrder})
    else:
        return  redirect(curl)


def generateOTP(request):
    if request.method=='POST':
        name=request.POST.get('name');
        print("Ajax is running")
        print(name)

class Checkout:
    def display(self,request):
        print("Hello")
        self.dishes = json.loads(request.POST.get('dishes'))
        self.totalAmount = list(map(str,request.POST.get('totalAmount').split()))[1]
        self.deliveryCharges = list(map(str,request.POST.get('deliveryCharges').split()))[1]
        self.packingCharges = list(map(str,request.POST.get('packingCharges').split()))[1]
        self.manualAddress = request.POST.get('manualAddress');
        self.addressLink = request.POST.get('addressLink');
        self.deliveryInstructions = request.POST.get('deliveryInstructions');
        orderIdQuery = "select MAX(orderId) from orders "
        models.cursor.execute(orderIdQuery)
        self.orderId=models.cursor.fetchall()[0][0]
        self.param_dict={
            'MID':'nrEAbc31174422501459',
            'ORDER_ID':str(int(self.orderId)+1),
            'TXN_AMOUNT':str(int(self.totalAmount)+int(self.deliveryCharges)+int(self.packingCharges)),
            'CUST_ID':str(request.COOKIES['email']),
            'INDUSTRY_TYPE_ID':'Retail',
            'WEBSITE':'WEBSTAGING',
            'CHANNEL_ID':'WEB',
            'CALLBACK_URL':curl+'myuser/checkout/',
        }
        self.param_dict['CHECKSUMHASH']=paytm.generate_checksum(self.param_dict,MERCHANT_KEY)
        return JsonResponse({'o':1})


    @csrf_exempt
    def checkout(self,request):
        [username, temp] = list(map(str, str(request.COOKIES['email']).split("@")))
        print(len(self.dishes))
        print("total : ",self.totalAmount)
        amount={ "totalAmount":self.totalAmount,"deliveryCharges":self.deliveryCharges,"packingCharges":self.packingCharges}
        if request.method=="GET":
            return render(request,"paytm.html",{"param_dict":self.param_dict})
        else:
            form=request.POST
            print(form)
            response_dict=dict()
            for i in form.keys():
                response_dict[i]=form[i]
                if i == 'CHECKSUMHASH' :
                    checksum=form[i]
            verify=paytm.verify_checksum(response_dict,MERCHANT_KEY,checksum)
            print("verify : ",verify)
            if verify:
                if response_dict ['RESPCODE']=='01':
                    orderStatus=1
                    response=render(request, "checkout.html", {'status': orderStatus})
                    response.set_cookie('order', 1)
                    if response_dict['PAYMENTMODE'] == "CC":
                        paymenMode = "Credit Card"
                    elif response_dict['PAYMENTMODE'] == "DC":
                        paymenMode = "Debit Card"
                    elif response_dict['PAYMENTMODE'] == "NB":
                        paymenMode = "Net Banking"
                    else:
                        paymenMode = "Paytm Wallet"

                else:
                    orderStatus=0
                    paymenMode="Online"
                    response=render(request, "checkout.html", {'status': orderStatus,'curl':curl})
                    print("order was not successfull because "+response_dict['RESPMSG'])



            query = "insert into orders values(NULL,'%s','%s','%d','%s','%s','%s','%s','%s','%s')" % (username, self.dishes,orderStatus,json.dumps(amount),response_dict ['TXNID'],time.asctime(time.localtime(time.time())),self.manualAddress,paymenMode,"0")
            models.cursor.execute(query)
            models.db.commit()

            query = "insert into payment values('%s','%s','%s','%s','%s','%s','%s','%s')" % (response_dict['ORDERID'],response_dict['TXNID'],response_dict['TXNAMOUNT'],response_dict['PAYMENTMODE'],response_dict['TXNDATE'],response_dict['BANKNAME'],response_dict['BANKTXNID'],response_dict['STATUS'])
            models.cursor.execute(query)
            models.db.commit()

            query = "insert into currentorder values('%s','%s','%d','%s','%s')" % (username,response_dict['ORDERID'],1,"CONFIRMED IT",time.asctime(time.localtime(time.time()+60*40)))
            models.cursor.execute(query)
            models.db.commit()
        return response

def orderList(request):
    if 'email' in request.COOKIES:
        userId = request.COOKIES['email'].split('@')[0]
        orderQuery="select orderId,orderTime,orderItem from orders where userId = '%s' ORDER BY orderId DESC"%(userId)
        models.cursor.execute(orderQuery)
        orders=list(map(list,models.cursor.fetchall()))
        for i in range(len(orders)):
            for j in range(len(orders[i])):
                if j==1:
                    print(orders[i][j])
                    t = orders[i][j].split()
                    t[3],t[1]=t[1],t[3]
                    if int(t[1][:2])>=12:
                        hour=int(t[1][:2])%12
                        t[1]=str(hour)+t[1][2:5]+" PM"
                    else:
                        t[1]=t[1][:5]+" AM"
                    orders[i][j]=t
                    print(orders[i][j])
                    print()
                elif j==2 :
                    orders[i][j]=json.loads(orders[i][j])
                    dish=list(orders[i][j].keys())
                    if len(dish) >= 2:
                        [item1, item2] = dish[:2]
                        temp = dict()
                        temp[item1] = orders[i][j][item1]
                        temp[item2] = orders[i][j][item2]
                        orders[i][j] = temp

        return render(request,'orderlist.html',{'curl':curl,'quickMenuFood':globalFoodData,'notifications':notifications,'orders':orders,'currentOrder':currentOrder})


def orderDetails(request):
    orderId=request.POST.get('orderId')
    print(orderId)
    orderQuery="select * from orders where orderId = '%s' "%(orderId)
    models.cursor.execute(orderQuery)
    orderDetails=list(models.cursor.fetchall()[0])

    t = orderDetails[6].split()
    t.sort()
    t[1], t[4] = t[4], t[1]
    if int(t[0][:2]) >= 12:
        hour = int(t[0][:2]) % 12
        t[0] = str(hour) + t[0][2:5] + " PM"
    else:
        t[0] = t[0][:5] + " AM"
    orderDetails[6] = t
    orderDetails[2] = json.loads(orderDetails[2])
    orderDetails[4] = json.loads((orderDetails[4]))
    orderDetails[7] = json.loads((orderDetails[7]))

    print(orderDetails)
    return JsonResponse({"orderDetails":orderDetails})

def lounchFeedback(request):
    if request.method=="GET":
        return render(request,"lounchfeedback.html",{'curl':curl,'quickMenuFood':globalFoodData,'notifications':notifications,'currentOrder':currentOrder})
    else:
        rateValue=request.POST.get('rateValue')
        fdback=request.POST.get('fdback')
        userId=request.COOKIES['email'].split('@')[0].lower()
        query="select rate from ratting where userId='%s' "%(userId)
        models.cursor.execute(query)
        rattingExist=models.cursor.fetchall()
        print(rattingExist)
        if rattingExist:
            rateValue=(rattingExist[0][0]+int(rateValue))/2
            query = "update ratting set rate='%f',feedback='%s' where userId='%s' " % (float(rateValue),fdback,userId)
            models.cursor.execute(query)
            models.db.commit()
        else:
            query = "insert into ratting values('%s','%f','%s')" % (userId,int(rateValue),fdback)
            models.cursor.execute(query)
            models.db.commit()
        return render(request, "lounchfeedback.html",{'curl': curl, 'quickMenuFood': globalFoodData, 'notifications': notifications,'currentOrder':currentOrder})


def trackOrder(request):
    query="select * from currentorder where userId='%s' "%(request.COOKIES['email'].split('@')[0].lower())
    models.cursor.execute(query)
    currentOrderData=models.cursor.fetchall()[0]
    status=currentOrderData[2]
    arrivalTime=currentOrderData[4]
    orderId=currentOrderData[1]
    return render(request,'trackorder.html',{'curl':curl,'currentOrder':currentOrder,'status':status,'arrivalTime':arrivalTime,'orderId':orderId})