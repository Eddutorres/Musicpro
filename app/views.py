from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def contacto(request):
    return render(request, 'app/contacto.html')

def catalogo(request):
    return render(request, 'app/catalogo.html')

def nosotros(request):
    return render(request, 'app/nosotros.html')