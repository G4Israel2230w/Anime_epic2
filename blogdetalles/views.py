from django.shortcuts import render
from .models import *
# Create your views here.

def base(request):
    return render(request, 'base.html',{} )

def blogdetalles(request):
    blog = Blogdetalles.objects.all()
    comment = Comment.objects.all()
    resumen=Resumen.objects.all()
    return render(request, 'blog-details.html', {
        'imagenBlog_1':blog,
        'comentario_1': comment,
        'resumen_1':resumen,
    } )