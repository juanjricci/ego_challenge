from rest_framework import viewsets, filters, status
from .models import Modelo, Componente, Ficha
from .serializers import ModeloSerializer, ComponenteSerializer, FichaSerializer
from rest_framework.response import Response
import json


class ModeloView(viewsets.ModelViewSet):
    serializer_class = ModeloSerializer
    queryset = Modelo.objects.all()

class ComponenteView(viewsets.ModelViewSet):
    serializer_class = ComponenteSerializer
    queryset = Componente.objects.all()

class FichaView(viewsets.ModelViewSet):
    serializer_class = FichaSerializer
    queryset = Ficha.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        new_ficha = Ficha.objects.create(
            imagen_url=data["imagen_url"],
            titulo=data["titulo"],
            descripcion=data["descripcion"],
            modelo=Modelo.objects.get(pk=data["modelo"])
        )
        componentes = json.loads(data["componentes"])
        print(componentes)

        for componente in componentes:
            comp_obj = Componente.objects.get(titulo=componente["titulo"])
            new_ficha.componentes.add(comp_obj)
        
        new_ficha.save()
        serializer = FichaSerializer(new_ficha)
        return Response(serializer.data)