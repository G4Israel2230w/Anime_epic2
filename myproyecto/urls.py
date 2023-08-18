"""
URL configuration for myproyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app import views
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index.html'),
    path('index.html', views.index, name='index.html'),
    path('base/', views.index, name='base.html'),
    path('', include ('categories.urls')),
    path('', include ('blog.urls')), 
    path('anime-watching.html', views.whatching, name='anime-watching.html'),
    path('anime-details.html', views.details, name='anime-details.html'),
    path('', include ('blogdetalles.urls')),
    path('login.html', views.login, name='lgon.html'),
    path('', include ('register.urls')),
    path('admin/', admin.site.urls),
    
]
if 1==1:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
    
