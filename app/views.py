from django.shortcuts import render
# Create your views here.
from .models import *
from .models import Video


def index(request):
    hero_items = HeroItem.objects.all()
    trending_products = TrendingProduct.objects.all()
    top_views = TopView.objects.all()
    new_comments = NewComment.objects.all()

    return render(request, 'index.html', {
        'hero_items': hero_items,
        'trending_products': trending_products,
        'top_views': top_views,
        'NewComment': new_comments
    })

def categories(request):
    return render(request,"categories.html",{} )

def base(request):
    return render(request, 'base.html',{} )


def whatching(request): 
    anime = Anime.objects.all()
    videos = Video.objects.all()
    episodes = Episode.objects.all()
    reviews = Review.objects.all()
    return render(request, 'anime-watching.html', {
        'anime_1': anime,
        'Episode_1': episodes,
        'Review': reviews,
        'video_1': videos,
    })
def details(request):
    return render(request, 'anime-details.html',{} )


def login(request):
    return render(request, 'login.html',{} )

 
