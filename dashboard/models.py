from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم الجهاز")
    location = models.CharField(max_length=150, verbose_name="الموقع")
    is_connected = models.BooleanField(default=True, verbose_name="متصل؟")
    last_connection = models.DateTimeField(auto_now=True, verbose_name="آخر اتصال")

    def __str__(self):
        return self.name

class Event(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='events', verbose_name="الجهاز")
    title = models.CharField(max_length=150, default="تم رصد شخص", verbose_name="عنوان الحدث")
    distance = models.FloatField(verbose_name="المسافة بالأتار")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ ووقت الحدث")
    image_url = models.URLField(default="https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=400", verbose_name="رابط الصورة")
    is_read = models.BooleanField(default=False, verbose_name="مقروء؟")

    def __str__(self):
        return f"{self.title} - {self.device.name} ({self.timestamp.strftime('%Y-%m-%d %H:%M')})"