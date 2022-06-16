from django.views.generic import ListView, DetailView
from product.models import Product
# Create your views here.

class ProductLV(ListView):
    model = Product

class ProductDV(DetailView):
    model = Product
