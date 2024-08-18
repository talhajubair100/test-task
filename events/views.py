from django.shortcuts import render
from django.utils import timezone
from .models import *
# Create your views here.
def home(request):
    today = timezone.now().date()
    events = Event.objects.filter(date__gte=today).order_by('?')[:6]
    context = {'events': events}
    return render(request, 'frontend/home.html', context)

def events(request):
    today = timezone.now().date()
    events = Event.objects.filter(date__gte=today).order_by('?')
    context = {'events': events}
    return render(request, 'frontend/events.html', context)

def event_details(request, id):
    event = Event.objects.get(id=id)
    context = {'event': event}
    return render(request, 'frontend/event_details.html', context)