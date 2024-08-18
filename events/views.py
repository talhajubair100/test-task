from django.shortcuts import render, redirect
from django.utils import timezone
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

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

@login_required(login_url='account_login')
def user_register_event(request):
    today = timezone.now().date()
    event_id = request.GET.get('event_id')
    event = Event.objects.get(id=event_id)
    user = request.user
    if event.date < today:
        messages.error(request, 'Event date has passed')
        return redirect('events')
    
    if event.booking_slots >= event.slots:
        messages.error(request, 'Event is full')
        return redirect('events')
    
    if UserRegistration.objects.filter(user=user, event=event).exists():
        messages.error(request, 'You are already registered for this event')
        return redirect('events')
    
    event.booking_slots += 1
    event.save()
    
    registration = UserRegistration.objects.create(user=user, event=event)
    registration.save()
    return redirect('user_events')

@login_required(login_url='account_login')
def user_unregister_event(request):
    today = timezone.now().date()
    event_id = request.GET.get('event_id')
    event = Event.objects.get(id=event_id)
    user = request.user
    if event.date < today:
        messages.error(request, 'Event date has passed')
        return redirect('user_events')
    if event.booking_slots > 0:
        event.booking_slots -= 1
        event.save()
    registration = UserRegistration.objects.get(user=user, event=event)
    registration.delete()
    return redirect('user_events')

@login_required(login_url='account_login')
def user_events(request):
    user = request.user
    events = UserRegistration.objects.filter(user=user)
    context = {'events': events}
    return render(request, 'frontend/user_events.html', context)


def search_events(request):
    query = request.GET.get('query')
    events = Event.objects.filter(Q(title__icontains=query) | Q(location__icontains=query))
    context = {'events': events}
    return render(request, 'frontend/events.html', context)