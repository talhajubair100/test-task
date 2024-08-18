from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('events/', events, name='events'),    
    path('event_details/<int:id>', event_details, name='event_details'),
    
    
]