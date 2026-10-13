from django.shortcuts import render, get_object_or_404
from .models import Device, Event
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def record_event_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            device_id = data.get('device_id')
            distance = float(data.get('distance', 0.0))
            
            device = Device.objects.get(id=device_id)
            
            if distance <= 3.0:
                title = "خطر شديد: اقتراب شخص جداً"
            else:
                title = "تحذير: شخص في منطقة الاقتراب"
                
            event = Event.objects.create(
                device=device,
                title=title,
                distance=distance
            )
            return JsonResponse({'status': 'success', 'event_id': event.id})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)


def index(request):
    total_alerts = Event.objects.count()
    detected_persons = Event.objects.filter(title__contains="شخص").count()
    active_days = 15 
    latest_event = Event.objects.last()
    
    context = {
        'total_alerts': total_alerts,
        'detected_persons': detected_persons,
        'active_days': active_days,
        'latest_event': latest_event,
    }
    return render(request, 'dashboard/index.html', context)

def events(request):
    events_list = Event.objects.all().order_by('-timestamp')
    return render(request, 'dashboard/events.html', {'events': events_list})

def event_detail(request, event_id=None):
    if event_id:
        event = get_object_or_404(Event, id=event_id)
    else:
        event = Event.objects.last()
    return render(request, 'dashboard/event_detail.html', {'event': event})

def live_stream(request):
    latest_device = Device.objects.first()
    return render(request, 'dashboard/live_stream.html', {'device': latest_device})

def devices(request):
    devices_list = Device.objects.all()
    return render(request, 'dashboard/devices.html', {'devices': devices_list})

def stats(request):
    total_alerts = Event.objects.count()
    return render(request, 'dashboard/stats.html', {'total_alerts': total_alerts})

def alerts(request):
    alerts_list = Event.objects.all().order_by('-timestamp')
    return render(request, 'dashboard/alerts.html', {'alerts': alerts_list})

def monthly_report(request):
    total_alerts = Event.objects.count()
    detected_persons = Event.objects.filter(title__contains="شخص").count()
    return render(request, 'dashboard/monthly_report.html', {
        'total_alerts': total_alerts,
        'detected_persons': detected_persons
    })

def settings(request):
    return render(request, 'dashboard/settings.html')

def login_view(request):
    return render(request, 'dashboard/login.html')