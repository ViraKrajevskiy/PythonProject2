from django.shortcuts import render
from .models import *

def index(request):
    caride = Car.objects.all()
    carmodel = CarModel.objects.all()

    context = {
        "caride": caride,
        "carmodel": carmodel,
        "title": "Course and Students"
    }
    return render(request, 'super.html', context=context)

def carmodel(request,model_id):
    caride = Car.objects.filter(model=model_id)
    carmodel = CarModel.objects.all()

    context = {
        "caride": caride,
        "carmodel": carmodel,
    }
    return render(request, 'Findpage.html', context=context)


def new_bot(request,new_id):
    caride = Car.objects.get(pk=new_id)
    carmodel = CarModel.objects.all()
    context = {
        "caride": caride,
        "carmodel":carmodel,
    }
    return render(request, 'about.html', context=context)