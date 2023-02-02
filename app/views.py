from django.shortcuts import render
from .models import Producto
from django.http import JsonResponse
import json
from rest_framework import viewsets
from .serializers import ProductoSerializer

import requests

# Create your views here.

class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

def home(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/home.html', data)

def contacto(request):
    return render(request, 'app/contacto.html')

def catalogo(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/catalogo.html', data)

def nosotros(request):
    return render(request, 'app/nosotros.html')

def carro(request):
    SKU=request.GET["sku"]
    productos=Producto.objects.filter(SKU__icontains=SKU)
    data = {
        'productos': productos
    }
    return render(request, 'app/carro.html', data)

def producto(request):
    SKU=request.GET["sku"]
    productos=Producto.objects.filter(SKU__icontains=SKU)
    data_prod = {
        'productos': productos
    }
    return render(request, 'app/producto.html', data_prod)

def euro(request):
    response=requests.get('https://api.cmfchile.cl/api-sbifv3/recursos_api/euro?apikey=fac1d9b01370e39370f86a5e9f2aa1a7081f4acf&formato=json').json
    return render(request, 'app/euro.html', {'response':response})



