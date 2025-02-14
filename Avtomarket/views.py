from django.shortcuts import render
from .models import *

def index(request):
    news = Avtosalon.objects.all()
    context = {
        "news":news,
        "title":"News Title"
    }
    return render(request,'News/index.html',context= context)

def car(request):
    mew = Car.objects.all()
    contect = {
        "news":mew,
        "title":"user"
    }
    return render(request,'News/index.html',context= contect)