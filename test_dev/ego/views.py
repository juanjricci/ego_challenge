from rest_framework import viewsets, filters
from .models import Modelo, Componente, Ficha
from .serializers import ModeloSerializer, ComponenteSerializer, FichaSerializer
from rest_framework.response import Response
import json
from django_filters.rest_framework import DjangoFilterBackend


class ModeloView(viewsets.ModelViewSet):
    serializer_class = ModeloSerializer
    queryset = Modelo.objects.all()
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    # sort by anio or precio
    # e.g: http://127.0.0.1:8000/app/api/modelos/?ordering=precio
    ordering_fields = ['anio', 'precio']
    # filter by tipo
    # e.g: http://127.0.0.1:8000/app/api/modelos/?tipo=AUTO
    # for shared values
    # e.g: http://127.0.0.1:8000/app/api/modelos/?tipo__in=SUV,CROSSOVER
    filterset_fields = {
        'tipo': ["in", "exact"],
    }

class ComponenteView(viewsets.ModelViewSet):
    serializer_class = ComponenteSerializer
    queryset = Componente.objects.all()

class FichaView(viewsets.ModelViewSet):
    serializer_class = FichaSerializer
    queryset = Ficha.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        new_ficha = Ficha.objects.create(
            pk=data["pk"],
            imagen_url=data["imagen_url"],
            titulo=data["titulo"],
            descripcion=data["descripcion"],
            modelo=Modelo.objects.get(pk=data["modelo"]),
            subtitulo = data["subtitulo"],
            descripcion_sub = data["descripcion_sub"],
            imagen_sub_url = data["imagen_sub_url"],
            subtitulo_1 = data["subtitulo_1"],
            descripcion_sub_1 = data["descripcion_sub_1"],
            imagen_sub_1_url = data["imagen_sub_1_url"],
        )
        componentes = json.loads(data["componentes"])
        print(componentes)

        for componente in componentes:
            comp_obj = Componente.objects.get(titulo=componente["titulo"])
            new_ficha.componentes.add(comp_obj)
        
        new_ficha.save()
        serializer = FichaSerializer(new_ficha)
        return Response(serializer.data)