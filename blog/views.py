from django.shortcuts import render, redirect
from contactos.forms import ContactoForm
from .forms import CustomUserCreationForm
from menus.models import Menu
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.
def render_articles(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def crud(request):
    return render(request, 'crud.html')

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="index")
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)

def menus(request):
    menus = Menu.objects.all()
    return render(request, 'menus.html', {'menus': menus})

def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["form"] = formulario

    return render(request, 'contacto.html', data)


