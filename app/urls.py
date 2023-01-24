from django import views
from django.urls import path
from .views import euro, home, contacto, catalogo, nosotros, producto

urlpatterns = [
    path('', home, name="home"),
    path('contacto', contacto, name="contacto"),
    path('catalogo', catalogo, name="catalogo"),
    path('nosotros', nosotros, name="nosotros"),
    path('producto', producto, name="producto"),
    path('euro', euro, name='euro'),
]