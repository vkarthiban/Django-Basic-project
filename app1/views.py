from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import travelPlaces1,info,news,subscribe,aboutus,team,message,trip

info1 = info.objects.all()[0]

def index(requst):

    print("request.....................................",requst)
    des = travelPlaces1.objects.all()
    newss = news.objects.all()
    return render(requst,'index.html',{'des':des,'info':info1,'newss':newss})



def about(requst):

    print("request.....................................",requst)
    des = travelPlaces1.objects.all()
    about = aboutus.objects.all()[0]
    print("about.....................................",about)
    teams = team.objects.all()
    return render(requst,'about.html',{'des':des,'info':info1,"about":about,"team":teams})



def contact(requst):
    
    print("request.....................................",requst)
    des = travelPlaces1.objects.all()
    return render(requst,'contact.html',{'des':des,'info':info1})  




def destinations(requst):

    print("request.....................................",requst)
    des = travelPlaces1.objects.all()
    print("info........................................",info.objects.all())
    return render(requst,'destinations.html',{'des':des,'info':info1})



def elements(requst):

    print("request.....................................",requst)
    des = travelPlaces1.objects.all()
    return render(requst,'elements.html',{'des':des,'info':info1})

def newses(requst):

    print("request.....................................",requst)
    newss = news.objects.all()
    return render(requst,'news.html',{'newss':newss,'info':info1})    



def search(requst):
    print("request.....................................",requst.POST['City'])

    des = travelPlaces1.objects.filter(title=requst.POST['City'],subtitle=requst.POST['Departure'],price=requst.POST['Budget'])
    print(".................................................",travelPlaces1.objects.filter(title="thiruvanamalai"))
    return render(requst,"destinations.html",{"des":des,'info':info1})



def subscribing(requst):
    print("request.....................................",requst.POST['username'])
    print("request.....................................",requst.POST['emailid'])
    sub = subscribe.objects.create(name=requst.POST['username'],emailid=requst.POST['emailid'])
    de = {"emailid":requst.POST['emailid'],"desc":"you are get the latest trends & news to this mail"}
    return render(requst,'subscribe.html',{"de":de})



def messaging(requst):
    print("request.....................................",requst.POST['emailid'])
    print("request.....................................",requst.POST['subject'])
    print("request.....................................",requst.POST['message'])
    mes = message.objects.create(name=requst.POST['Name'],emailid=requst.POST['emailid'],subject=requst.POST['subject'],message=requst.POST['message'])
    return render(requst,'message.html')


