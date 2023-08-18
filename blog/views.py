from django.shortcuts import render

from .models import *



def blog(request):
    resumen_1 = Resumen.objects.all()
    anime_list = Anime.objects.all()  # Obtener todos los objetos 'Anime'

    context = {
        'resumen_1': resumen_1,
        'anime_1': anime_list,  # Pasar la lista de objetos 'Anime' al contexto
    }

    return render(request, 'blog.html', context)


