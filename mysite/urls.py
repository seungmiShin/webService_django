"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from mysite.views import HomeView
from mysite.views import UserCreateView, UserCreateDoneTV

from product.views import ProductLV, ProductDV
from coupon.views import CouponLV, CouponDV
from device.views import DeviceLV, DeviceDV

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(), name='home'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', UserCreateView.as_view(), name='register'),
    path('accounts/register/done', UserCreateDoneTV.as_view(), name='register_done'),

    path('product/', ProductLV.as_view(), name='product_index'),
    path('product/<int:pk>/', ProductDV.as_view(), name='product_detail'),

    path('coupon/', CouponLV.as_view(), name='coupon_index'),
    path('coupon/<int:pk>/', CouponDV.as_view(), name='coupon_detail'),

    path('device/', DeviceLV.as_view(), name='device_index'),
    path('device/<int:pk>/', DeviceDV.as_view(), name='device_detail')

]
