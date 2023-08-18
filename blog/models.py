from django.db import models

# Create your models here.


class Resumen (models.Model):
    titulo=models.CharField(max_length=100)
    texto=models.TextField()
    imagen=models.ImageField(upload_to='imagen_de_blog')
    class Meta:
        db_table = 'baseblog.bd' 

class Anime (models.Model):
    imagen1=models.ImageField(upload_to='imagen_anime')
    fecha=models.DateField()
    titulo1=models.CharField(max_length=150)
    class Meta:
        db_table = 'Animeblog.bd' 