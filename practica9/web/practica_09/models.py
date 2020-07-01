from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.
class GrupoMusical(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_fundacion = models.DateTimeField(default=timezone.now)
    estilo_musical = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre

class Album(models.Model):
    titulo = models.CharField(max_length=150) 
    distribuidora = models.CharField(max_length=200)
    fecha_lanzamiento = models.DateField()
    grupo = models.ForeignKey(GrupoMusical, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    def anio_publicacion(self):
        return datetime.now().year - self.fecha_lanzamiento.year 

class Instrumentos(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Musico(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    instrumento_principal = models.ForeignKey(Instrumentos, on_delete=models.CASCADE, related_name="principal")
    instrumentos_secundarios = models.ManyToManyField(Instrumentos, related_name="secundarios",blank=True)
    grupos_musicales = models.ManyToManyField(GrupoMusical)
    lugar_nacimiento = models.CharField(max_length=100,blank=True)
    latitud = models.FloatField(blank=True)
    longitud = models.FloatField(blank=True)

    def __str__(self):
        return self. nombre
    

