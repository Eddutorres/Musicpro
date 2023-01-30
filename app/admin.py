from django.contrib import admin
from .models import Categoria, Cliente, Marca, Producto, Venta, Bodegero,Boleta, Entrega

admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Venta)
admin.site.register(Bodegero)
admin.site.register(Boleta)
admin.site.register(Entrega)
admin.site.register(Marca)

# Register your models here.
