from django.views.generic import ListView, DetailView
from device.models import Device
# Create your views here.

class DeviceLV(ListView):
    model = Device

class DeviceDV(DetailView):
    model = Device
