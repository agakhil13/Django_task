from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.name = "Mumbai"
    dest1.desc = "The city never sleeps"
    dest1.price = 600
    dest2 = Destination()
    dest2.name = "Dhaka"
    dest2.desc = "Biggest City"
    dest2.price = 750
    dest3 = Destination()
    dest3.name = "Kolkata"
    dest3.desc = "Garden City"
    dest3.price = 450
    return render(request, 'index.html', {'dest1': dest1, 'dest2': dest2, 'dest3': dest3})