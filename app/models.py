from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    id_cli = models.IntegerField(primary_key=True, default='1')
    nombre = models.CharField(max_length=50)
    ap_pater_cli = models.CharField(max_length=50, null=True)
    ap_mater_cli = models.CharField(max_length=50, null=True)
    rut = models.CharField(max_length=20)
    direccion = models.TextField()

    def __str__(self):
        return self.nombre



class Producto(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.TextField()
    SKU = models.CharField(max_length=20, primary_key=True)
    precio = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, null=True)
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre

class Factura(models.Model):
    id_factura = models.IntegerField(primary_key=True)
    fecha = models.DateField()
    id_cli = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    total = models.IntegerField()

    def __str__(self):
        return self.id_factura

class Detalle_factura(models.Model):
    id_detalle = models.IntegerField(primary_key=True)
    id_factura = models.ForeignKey(Factura, on_delete=models.PROTECT)
    SKU = models.ForeignKey(Producto, on_delete=models.PROTECT )
    cantidad = models.IntegerField()

    def __str__(self):
        return self.id_detalle

