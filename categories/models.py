from django.db import models

# Create your models here.


class Anime_todo(models.Model):
    imagen=models.ImageField(upload_to='imagen_anime_todo')
    capitulos = models.CharField(max_length=10)
    comentarios = models.IntegerField()
    views = models.IntegerField()
    estado = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)

class TopView(models.Model):
    image = models.ImageField(upload_to='top_views')
    capitulos = models.CharField(max_length=10)
    vistas = models.IntegerField()
    Nombre = models.CharField(max_length=100)
    Dia = models.BooleanField(default=False)
    Semana = models.BooleanField(default=False)
    Mes = models.BooleanField(default=False)
    Años = models.BooleanField(default=False)

    