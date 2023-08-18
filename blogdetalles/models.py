from django.db import models

# Create your models here.
class Blogdetalles(models.Model):
    title = models.CharField(max_length=150)
    seccion = models.CharField(max_length=100, default='anime')
    date = models.DateField()
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images')

    def __str__(self):
        return self.title

class Resumen(models.Model):
    titulo= models.CharField(max_length=150)
    imagen= models.ImageField(upload_to='imagen_resumen')
    contenido= models.TextField()
    dato_extra1= models.CharField( max_length=50)
    dato_extra2= models.CharField( max_length=50)
    dato_extra3= models.CharField( max_length=50)

class Comment(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    