from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('events/', events, name='events'),    
    path('event_details/<int:id>', event_details, name='event_details'),
    path('user_register_event', user_register_event, name='user_register_event'),
    path('user_unregister_event', user_unregister_event, name='user_unregister_event'),
    path('user_events', user_events, name='user_events'),
    path('search_events', search_events, name='search_events'),
    
]