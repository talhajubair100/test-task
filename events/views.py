from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    events = Event.objects.filter().order_by('?')[:6]
    context = {'events': events}
    return render(request, 'frontend/home.html', context)
