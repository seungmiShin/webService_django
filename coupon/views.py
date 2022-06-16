from django.views.generic import ListView, DetailView
from coupon.models import Coupon
# Create your views here.

class CouponLV(ListView):
    model = Coupon

class CouponDV(DetailView):
    model = Coupon
