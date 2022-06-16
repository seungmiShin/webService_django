from django.contrib import admin

# Register your models here.
from django.contrib import admin
from product.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'release_date', 'created_date', 'image_name', 'url')
