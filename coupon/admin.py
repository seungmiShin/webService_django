from django.contrib import admin

# Register your models here.
from django.contrib import admin
from coupon.models import Coupon

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'image_name', 'created_date')
