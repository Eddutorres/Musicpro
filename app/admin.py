from django.contrib import admin
from .models import Categoria, Cliente, Marca, Producto, Detalle_factura, Factura

admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Factura)
admin.site.register(Detalle_factura)
admin.site.register(Marca)

# Register your models here.
