from django import views
from django.urls import path, include
from .views import euro, home, contacto, catalogo, nosotros, carro, producto, ProductoViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register('producto', ProductoViewset)


urlpatterns = [
    path('', home, name="home"),
    path('carro', carro, name="carro"),
    path('contacto', contacto, name="contacto"),
    path('catalogo', catalogo, name="catalogo"),
    path('nosotros', nosotros, name="nosotros"),
    path('producto', producto, name="producto"),
    path('euro', euro, name='euro'),
    path('api/', include(router.urls)),
]