from django.shortcuts import render, redirect, get_object_or_404
from contactos.forms import ContactoForm
from contactos.models import Contacto
from menus.carrito import Carrito
from .forms import CustomUserCreationForm, MenuForm
from menus.models import Menu
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from calificaciones.models import Menu, Review

# Create your views here.
def render_articles(request):
    menus = Menu.objects.all()
    return render(request, 'index.html', {'menus': menus})

def nosotros(request):
    return render(request, 'nosotros.html')

def crud(request):
    contactos = Contacto.objects.all()
    return render(request, 'crud.html', {'contactos': contactos})

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

def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se ha guardado tu contacto correctamente")
        else:
            data["form"] = formulario

    return render(request, 'contacto.html', data)

def agregar_menu(request, menu_id):
    carrito = Carrito(request)
    menu = Menu.objects.get(id=menu_id)
    carrito.agregar(menu)
    return redirect("menus")

def eliminar_menu(request, menu_id):
    carrito = Carrito(request)
    menu = Menu.objects.get(id=menu_id)
    carrito.eliminar(menu)
    return redirect("menus")

def restar_menu(request, menu_id):
    carrito = Carrito(request)
    menu = Menu.objects.get(id=menu_id)
    carrito.restar(menu)
    return redirect("menus")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("menus")

def agregar_producto(request):
    data = {
        'form': MenuForm()
    }
    if request.method == 'POST':
        formulario = MenuForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario
    return render(request, 'administracion/agregar.html', data)

def perfil(request):
    return render(request, 'perfil.html')

def modificar_producto(request, id):
    producto = get_object_or_404(Menu, id=id)
    data = {
        'form': MenuForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = MenuForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="menus")
        data["form"] = formulario
    return render(request, 'administracion/modificar_menu.html', data)

def menus(request):
    menus = Menu.objects.all()
    return render(request, 'menus.html', {'menus': menus})

def detalle_menu(request, id_menu):
    try:
        menu = Menu.objects.get(pk=id_menu)
        reviews = Review.objects.filter(menu=menu)
    except Menu.DoesNotExist:
        # Manejar el caso en el que el menú no se encuentre
        menu = None
        reviews = None
    return render(request, 'detalle_menu.html', {'menu': menu, 'reviews': reviews})
