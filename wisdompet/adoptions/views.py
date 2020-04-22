from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Pet


def home(request):
    pets = Pet.objects.all()
    return render(request,'adoptions/home.html',{'pets':pets})

def pet_details(request,id):
    try:
        pet = Pet.objects.get(id=id)
    except:
        raise Http404('Pet not found')
        
    return render(request,'adoptions/pet_details.html',{'pet':pet})

