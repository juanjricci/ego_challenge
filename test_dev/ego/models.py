from django.db import models

# Create your models here.
class Modelo(models.Model):

    auto = 'AUTO'
    pup = 'PICKUP'
    com = 'COMERCIAL'
    suv = 'SUV'
    xover = 'CROSSOVER'

    TIPO_OPS = (
        (auto, 'Auto'),
        (pup, 'Pickup'),
        (com, 'Comercial'),
        (suv, 'SUV'),
        (xover, 'Crossover'),
    )
    tipo = models.CharField(max_length=200, choices=TIPO_OPS, default=auto)
    modelo = models.CharField(max_length=200)
    anio = models.IntegerField()
    precio = models.DecimalField(max_digits=19, decimal_places=2)
    thumbnail_url = models.URLField(max_length=200)

    def __str__(self):
        # return str(self.pk)
        return self.modelo

class Componente(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen_url = models.URLField(max_length=200)

    def __str__(self):
        # return str(self.pk)
        return self.titulo

class Ficha(models.Model):
    imagen_url = models.URLField(max_length=200)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    modelo = models.OneToOneField(Modelo, on_delete=models.CASCADE)
    componentes = models.ManyToManyField(Componente)
    subtitulo = models.CharField(max_length=200)
    descripcion_sub = models.TextField()
    imagen_sub_url = models.URLField(max_length=200)
    subtitulo_1 = models.CharField(max_length=200)
    descripcion_sub_1 = models.TextField()
    imagen_sub_1_url = models.URLField(max_length=200)

    def __str__(self):
        return self.modelo.modelo