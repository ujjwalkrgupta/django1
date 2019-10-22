from django.shortcuts import render
from django.http import HttpResponse
from .models import destination

# Create your views here.
def index(request):

    dest1 = destination()
    dest1.name = 'mumbai'
    dest1.price = 700
    dest1.desc = 'city that never sleeps'
    
    return render(request, 'index.html',{'dest1':dest1})
