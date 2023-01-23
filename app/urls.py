from django.urls import path
from .views import home, contacto, catalogo, nosotros

urlpatterns = [
    path('', home, name="home"),
    path('contacto', contacto, name="contacto"),
    path('catalogo', catalogo, name="catalogo"),
    path('nosotros', nosotros, name="nosotros"),
]