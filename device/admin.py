from django.contrib import admin

# Register your models here.
from django.contrib import admin
from device.models import Device

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'release_date', 'image_name', 'created_date')
