from rest_framework import serializers
from .models import Modelo, Ficha, Componente

class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model=Modelo
        fields=('pk', 'tipo', 'modelo', 'anio', 'precio', 'thumbnail_url')

class ComponenteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Componente
        fields=('pk','titulo', 'descripcion', 'imagen_url')

class FichaSerializer(serializers.ModelSerializer):
    modelo = serializers.PrimaryKeyRelatedField(queryset=Modelo.objects.all())
    # modelo = ModeloSerializer(read_only=True)
    componentes = ComponenteSerializer(many=True, read_only=True)

    class Meta:
        model=Ficha
        fields=(
            'pk',
            'imagen_url',
            'titulo', 
            'descripcion', 
            'modelo', 
            'componentes',
            'subtitulo',
            'descripcion_sub',
            'imagen_sub_url',
            'subtitulo_1',
            'descripcion_sub_1',
            'imagen_sub_1_url'
            )
        depth = 1