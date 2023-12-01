from django.shortcuts import render,redirect
from .models import Destination,Sub,Booked
import random
from twilio.rest import Client
# Create your views here.


def doMessage(verifycode,phno):
  
    account_sid = 'AC5617d0a82e994143df0abc82008dfaf9'
    auth_token = '9f84a00af36f9686503e1b3c3a4be8d7'


    client = Client(account_sid, auth_token)

    to_phone_number = '+91'+str(phno)

    from_phone_number = '+15733832067'

    message = 'you have sucessfully booked the seat with registration no:'+ str(verifycode);
    message = client.messages.create(
        body=message,
        from_=from_phone_number,
        to=to_phone_number
    )
    print('SMS sent with SID:', message.sid)




def bookfun(request,place):
    if request.method=='POST':
        obj=Destination.objects.filter(name=place)
        name=request.POST['pname']
        age=request.POST['page']
        phno=request.POST['pphno']
        destini=request.POST['pdestini']
        date=request.POST['pdate']
        email=request.POST['pemail']
        bookobj=Booked(name=name,age=age,phno=phno,destini=destini,date=date,email=email)
        bookobj.save()
        verifycode=random.randrange(1000000,9999999)
        name=str.lower(name)
        doMessage(verifycode,phno)
        return render(request,'feedback.html',{'verifycode':verifycode,'name':name})
    else:
        place=str.lower(place)
        return render(request,'booking.html',{'place':place})
    

def index(request):
    dests = Destination.objects.all()
    return render(request, 'index.html', {'dests': dests})



        