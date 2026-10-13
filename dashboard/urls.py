# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='home'),
#     path('events/', views.events, name='events'),
#     path('event-detail/', views.event_detail, name='event_detail'),
#     path('live/', views.live_stream, name='live_stream'),
#     path('devices/', views.devices, name='devices'),
#     path('stats/', views.stats, name='stats'),
#     path('alerts/', views.alerts, name='alerts'),
#     path('report/', views.monthly_report, name='monthly_report'),
#     path('settings/', views.settings, name='settings'),
#     # path('login/', views.login_view, name='login'),
#     path('api/record-event/', views.record_event_api, name='record_event_api'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('events/', views.events, name='events'),
    path('event-detail/', views.event_detail, name='event_detail'),
    path('live/', views.live_stream, name='live_stream'),
    path('devices/', views.devices, name='devices'),
    path('stats/', views.stats, name='stats'),
    path('alerts/', views.alerts, name='alerts'),
    path('report/', views.monthly_report, name='monthly_report'),
    path('settings/', views.settings, name='settings'),
    path('devices/add/', views.add_device, name='add_device'),
    path('api/record-event/', views.record_event_api, name='record_event_api'),
]