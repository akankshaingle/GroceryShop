from django.shortcuts import render,redirect

from. import models
from django.conf import settings
import json
import random
from django.http.response import JsonResponse
from django.core.mail import send_mail
curl=settings.CURRENT_URL
class DpHome:
    def dpHome(self,request):
        if 'dpId' in request.COOKIES:
            dpId=request.COOKIES['dpId']
            query="select status from deliverypartner where dpId='%s'"%(dpId)
            query="select status from deliverypartner where dpId='%s'"%(dpId)
            models.cursor.execute(query)
            self.dpStatus=models.cursor.fetchall()[0][0]
            print("dpStatus : ",self.dpStatus)
            currentOrderQuery = "select * from currentdpstatus where dpId='%s'" % (dpId)
            models.cursor.execute(currentOrderQuery)
            currentOrder = models.cursor.fetchall()
            print(currentOrder)
            if currentOrder:
                print("status : ",self.dpStatus)
                print(currentOrder)
                currentOrder=currentOrder[0]
                self.orderStatus=currentOrder[3]
                print("Order Status:",self.orderStatus)
                userQuery="SELECT name,mobile from registration where userId = '%s' "%(currentOrder[1])
                models.cursor.execute(userQuery)
                [userName,userMobile]=list(models.cursor.fetchall()[0])

                orderQuery="SELECT orderItem,amount,address,paymentMode from orders where orderId = '%s' "%(currentOrder[2])
                models.cursor.execute(orderQuery)
                orderDetails=list(models.cursor.fetchall()[0])
                orderItem=json.loads(orderDetails[0])
                totalAmount=sum(map(float,json.loads(orderDetails[1]).values()))
                orderDetails[2]=json.loads(orderDetails[2])
                address=orderDetails[2]['doorNo']+','+orderDetails[2]['area']+' '+orderDetails[2]['landmark']+' '+orderDetails[2]['city']+','+orderDetails[2]['pincode']
                paymentMode=orderDetails[-1]
                orderItem=list(orderItem.values())
                print(orderItem)
                for i in range(len(orderItem)):
                    orderItem[i]=list(orderItem[i].values())
                    orderItem[i].append(float(orderItem[i][1])*float(orderItem[i][2]))
                self.orderDetails=[currentOrder[2],orderItem,totalAmount,address,paymentMode]
                self.userDetails=[userName,userMobile]
                print("dpStatus : ",self.dpStatus)
                return render(request,'dphome.html',{'curl':curl,'orderDetails':self.orderDetails,'userDetails':self.userDetails,'dpStatus':self.dpStatus,'noOfOrder':1,'orderStatus':self.orderStatus})
            else:
                return render(request,'dphome.html',{'curl':curl,'dpStatus':self.dpStatus,'noOfOrder':0,'orderStatus':0})
        else:
            return redirect(curl)

    def acceptOrder(self,request):
        orderId=request.POST.get('orderId')

        query = "UPDATE currentorder SET status = '%d' WHERE orderId = '%s' " % (4, orderId)
        models.cursor.execute(query)
        models.db.commit()

        self.orderStatus=1

        query = "UPDATE currentdpstatus SET status='%d' where orderId='%s' " % (1,orderId)
        models.cursor.execute(query)
        models.db.commit()

        return JsonResponse({'op':1})

    def pickUpOrder(self,request):
        orderId = request.POST.get('orderId')

        query = "UPDATE currentorder SET status = '%d' WHERE orderId = '%s' " % (5,orderId)
        models.cursor.execute(query)
        models.db.commit()

        query = "UPDATE currentdpstatus SET status='%d' where orderId='%s' " % (2,orderId)
        models.cursor.execute(query)
        models.db.commit()

        return JsonResponse({'op':1})

    def deliveredOrder(self,request):
        orderId = request.POST.get('orderId')

        query = "DELETE from currentorder WHERE orderId = '%s' " % (orderId)
        models.cursor.execute(query)
        models.db.commit()

        query = "DELETE from currentdpstatus where orderId='%s' " % (orderId)
        models.cursor.execute(query)
        models.db.commit()

        return JsonResponse({'op':1})

    def cancelOrder(self,request):
        orderId=request.POST.get('orderId')
        query="UPDATE currentorder SET status = '%d' WHERE orderId = '%s' "%(2,orderId)
        models.cursor.execute(query)
        models.db.commit()

        query="DELETE from currentdpstatus where orderId='%s' "%(orderId)
        models.cursor.execute(query)
        models.db.commit()

        query = "UPDATE orders SET  deliveryPartnerId = '%s' WHERE orderId  = '%s' " % (' ', orderId)
        models.cursor.execute(query)
        models.db.commit()

        print(orderId)
        return JsonResponse({'op':1})

def changeStatus(request):
    if 'dpId' in request.COOKIES:
        status=int(request.POST.get('status'))
        dpId=request.COOKIES['dpId']
        query="UPDATE deliverypartner SET status = '%d' WHERE dpId = '%s' "%(status,dpId)
        models.cursor.execute(query)
        models.db.commit()
    return JsonResponse({'op':1})

class EditProfile:
    def displayInfo(self,request):
        if 'dpId' in request.COOKIES:
            dpId = request.COOKIES['dpId']
            query = "SELECT * from deliverypartner WHERE dpId='%s' " % (dpId)
            models.cursor.execute(query)
            Details = models.cursor.fetchall()[0]
            dpDetails = dict()
            dpDetails['name'] = Details[1]
            dpDetails['email'] = Details[2]
            self.password=Details[3]
            # self.email='akaushal451@gmail.com'
            self.email=dpDetails['email']
            dpDetails['mobile'] = Details[4]
            dpDetails['gender'] = Details[5]
            dpDetails['address'] = Details[6]
            dpStatus = Details[8]
            return render(request, 'dpEditProfile.html', {'curl': curl, 'dpDetails': dpDetails, 'dpStatus': dpStatus})
        else:
            return redirect(curl)

    def saveInfo(self,request):
        print("SaveInfo has called")
        if request.method=='POST':
            name=request.POST.get('dpName')
            address=request.POST.get('dpAddress')
            gender=request.POST.get('dpGender')
            updateQuery="UPDATE deliverypartner SET dpName='%s',dpAddress='%s',dpgender='%s',dpPassword='%s' WHERE dpId='%s'"%(name,address,gender,self.password,request.COOKIES['dpId'])
            models.cursor.execute(updateQuery)
            models.db.commit()
            return redirect(curl)
        else:
            return render(request,"edit_info.html",{'curl':curl})

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
        to = self.email
        send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])

    def getOtp(self,request):
        print("getOtp has called")
        self.sendOtp()
        print("OTP : ",self.otp)
        self.newPassword=request.POST.get('password')
        return JsonResponse({'otp':1})

    def resendOtp(self,request):
        print("ResendOtp has called")
        self.sendOtp()
        print("REsend OTP :",self.otp)
        return JsonResponse({'otp':1})

    def checkOtp(self,request):
        print("CheckOtp has called")
        otp=request.POST.get('otp')
        print(otp)
        print(self.otp)
        if int(otp)==int(self.otp):
            print("OTP is same")
            self.password=self.newPassword
            return JsonResponse({"otpValue":1,"password":self.newPassword})
        else:
            print("OTP is diffrent")
            return JsonResponse({"otpValue":0})

def previousOrders(request):
    dpId=request.COOKIES['dpId']
    query = "select status from deliverypartner where dpId='%s'" % (dpId)
    models.cursor.execute(query)
    dpStatus = models.cursor.fetchall()[0][0]

    query="select orderId,userId,orderTime,address,paymentMode,orderStatus from orders WHERE deliveryPartnerId = '%s' "%(dpId)
    models.cursor.execute(query)
    orders=list(map(list,models.cursor.fetchall()))

    if orders:
        for i in range(len(orders)):
            query = "SELECT name from registration WHERE userId='%s' " % (orders[i][1])
            models.cursor.execute(query)
            orders[i][1] = models.cursor.fetchall()[0][0]

            t = orders[i][2].split()
            t[3], t[1] = t[1], t[3]
            if int(t[1][:2]) >= 12:
                hour = int(t[1][:2]) % 12
                t[1] = str(hour) + t[1][2:5] + " PM"
            else:
                t[1] = t[1][:5] + " AM"
            orders[i][2] = t

            orders[i][3] = list(json.loads(orders[i][3]).values())
        print(orders)
        print("kdf")
        return render(request, 'previousorder.html',{'curl': curl, 'dpStatus': dpStatus, 'noOfOrder': 1, 'orders': orders})
    else:
        return render(request, 'previousorder.html',{'curl': curl, 'dpStatus': dpStatus, 'noOfOrder': 0, 'orders': orders})

def logout(request):
    if 'dpId' in request.COOKIES:
        dpId=request.COOKIES['dpId']
        query = "UPDATE deliverypartner SET status = '%d' WHERE dpId = '%s' " % (0, dpId)
        models.cursor.execute(query)
        models.db.commit()

        response=redirect(curl+'')
        response.delete_cookie('dpId')
        return response
    else:
        return redirect(curl + '')
