from django.db import models

# Create your models here.

class Imagen(models.Model):
    imagen_2=models.ImageField(upload_to='imagen_de_blog')
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    