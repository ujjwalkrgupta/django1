from django.shortcuts import render
from django.http import HttpResponse
from .models import destination

# Create your views here.
def index(request):

    dest1 = destination()
    dest1.name = 'mumbai'
    dest1.price = 700
    dest1.img = 'destination_1.jpg'
    dest1.desc = 'city that never sleeps'

    dest2 = destination()
    dest2.name = 'kolkata'
    dest2.img = 'destination_2.jpg'
    dest2.price = 800
    dest2.desc = 'city of joy'

    dest3 = destination()
    dest3.name = 'bangalore'
    dest3.img = 'destination_3.jpg'
    dest3.price = 900
    dest3.desc = 'silicon valley of india'

    dests =[dest1,dest2,dest3]

    
    return render(request, 'index.html',{'dests':dests})
