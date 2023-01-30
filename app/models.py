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
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=20)
    direccion = models.TextField()
    registrado = models.BooleanField()

    def __str__(self):
        return self.nombre



class Producto(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.TextField()
    SKU = models.CharField(max_length=20)
    precio = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, null=True)
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    fecha = models.DateField()
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cant_productos = models.IntegerField()
    tipo_tarjeta = models.CharField(max_length=20)
    total = models.IntegerField()

    def __str__(self):
        return self.fecha

class Boleta(models.Model):
    fecha = models.DateField()
    num_boleta = models.IntegerField()
    total = models.IntegerField()
    venta = models.ForeignKey(Venta, on_delete=models.PROTECT)

    def __str__(self):
        return self.num_boleta

class Bodegero(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Entrega(models.Model):
    fecha_entrega = models.DateField()
    boleta = models.ForeignKey(Boleta, on_delete=models.PROTECT)
    id_venta = models.ForeignKey(Venta, on_delete=models.PROTECT)
    rut_cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    rut_bodeguero = models.ForeignKey(Bodegero, on_delete=models.PROTECT)

    def __str__(self):
        return self.fecha_entrega

    
    