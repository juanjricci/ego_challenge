from rest_framework import serializers
from .models import Modelo, Ficha, Componente

class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model=Modelo
        fields=('tipo', 'modelo', 'anio', 'precio', 'thumbnail')

class ComponenteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Componente
        fields=('titulo', 'descripcion', 'imagen')

class FichaSerializer(serializers.ModelSerializer):
    modelo = serializers.PrimaryKeyRelatedField(queryset=Modelo.objects.all())
    # modelo = ModeloSerializer(read_only=True)
    componente = ComponenteSerializer(many=True, read_only=True)

    class Meta:
        model=Ficha
        fields=('imagen', 'descripcion', 'modelo', 'componente')