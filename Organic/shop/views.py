from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
# Create your views here.

def catalog(request):
    products = Products.objects.all()
    return render(request, 'catalog.html', {'products': products})