from django.contrib import admin
from .models import Device, Event

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'is_connected', 'last_connection')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'device', 'distance', 'timestamp', 'is_read')
    list_filter = ('is_read', 'device')