from rest_framework import viewsets, filters, status
from .models import Modelo, Componente, Ficha
from .serializers import ModeloSerializer, ComponenteSerializer, FichaSerializer
from rest_framework.response import Response


class ModeloView(viewsets.ModelViewSet):
    serializer_class = ModeloSerializer
    queryset = Modelo.objects.all()

class ComponenteView(viewsets.ModelViewSet):
    serializer_class = ComponenteSerializer
    queryset = Componente.objects.all()

class FichaView(viewsets.ModelViewSet):
    serializer_class = FichaSerializer
    queryset = Ficha.objects.all()