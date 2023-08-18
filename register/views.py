from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib import messages
from .models import *
# Create your views here.

def Imagen_23(request):
    imagenes = Imagen.objects.all()
    return render(request, 'signup.html', {'imagen_1': imagenes})

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            messages.success(request, f'Usuario {usuario} creado')
            return redirect('index')

    else:
        form = UserRegisterForm()
    
    return render(request, 'signup.html', {'form': form}) 



 