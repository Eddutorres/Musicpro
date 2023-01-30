from .models import Producto
from rest_framework import serializers


class ProductoSerializer(serializers.ModelSerializer):
    nombre_marca = serializers.CharField(read_only=True, source="marca.nombre")
    nombre_categoria = serializers.CharField(read_only=True, source="categoria.nombre")
    class Meta:
        model = Producto
        fields = '__all__'
