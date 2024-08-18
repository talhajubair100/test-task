from django.contrib import admin
from .models import Event, UserRegistration
# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time', 'location', 'slots', 'booking_slots')
    search_fields = ('title', 'description')
    
@admin.register(UserRegistration)
class UserRegistrationAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'registration_date')
    list_filter = ('event', 'registration_date')