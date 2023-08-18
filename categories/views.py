from django.shortcuts import render
from .models import *
# Create your views here.


def categories(request):
    anime_todo = Anime_todo.objects.all()
    top_views = TopView.objects.all()
    return render(request, 'categories.html',{
        'anime_1':anime_todo,
        'top_videos':top_views,

    })  