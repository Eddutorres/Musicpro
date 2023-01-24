from django.shortcuts import render

import requests

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def contacto(request):
    return render(request, 'app/contacto.html')

def catalogo(request):
    return render(request, 'app/catalogo.html')

def nosotros(request):
    return render(request, 'app/nosotros.html')

def producto(request):
    return render(request, 'app/producto.html')

def euro(request):
    response=requests.get('https://api.cmfchile.cl/api-sbifv3/recursos_api/euro?apikey=fac1d9b01370e39370f86a5e9f2aa1a7081f4acf&formato=json').json
    return render(request, 'app/euro.html', {'response':response})