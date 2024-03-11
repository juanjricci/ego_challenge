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
    thumbnail = models.ImageField(upload_to='car_thumbnails', blank=True)

    def __str__(self):
        # return str(self.pk)
        return self.modelo

class Componente(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='components_images')

    def __str__(self):
        # return str(self.pk)
        return self.titulo

class Ficha(models.Model):
    imagen = models.ImageField(upload_to='car_images')
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    modelo = models.OneToOneField(Modelo, on_delete=models.CASCADE)
    componentes = models.ManyToManyField(Componente)

    def __str__(self):
        return self.modelo.modelo