from django.shortcuts import render
from .models import Airplane,Flights

# Create your views here.
def index(request):

    return render(request,"flight/index.html",{
        'flight': Flights.objects.all()
    })