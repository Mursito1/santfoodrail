from django.shortcuts import render, redirect, get_object_or_404
from contactos.forms import ContactoAdminForm, ContactoForm
from contactos.models import Contacto
from menus.carrito import Carrito
from pedidos.models import Pedido, PedidoItem
from .forms import CustomUserCreationForm, MenuForm
from menus.models import Menu
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


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

@login_required
def menus(request):
    menus = Menu.objects.all()
    return render(request, 'menus.html', {'menus': menus})

def editar_contacto(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    if request.method == "POST":
        form = ContactoAdminForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            return redirect('crud')
    else:
        form = ContactoAdminForm(instance=contacto)
    return render(request, 'administracion/modificar_contacto.html', {'form': form, 'contacto': contacto})

def pago(request):
        carrito = Carrito(request)
        contenido_carrito = carrito.carrito.values()
        return render(request, 'pago.html', {'contenido_carrito': contenido_carrito})

def guardar_pedido(request):
    if request.method == "POST":
        carrito = request.session.get("carrito", {})
        if carrito:
            pedido = Pedido.objects.create(user=request.user)  # Asumiendo que hay un usuario logueado
            for item in carrito.values():
                PedidoItem.objects.create(
                    pedido=pedido,
                    menu_id=item["menu_id"],
                    nombre=item["nombre"],
                    precio=item["acumulado"],
                    cantidad=item["cantidad"],
                )
            # Limpiar el carrito después de guardar el pedido
            request.session["carrito"] = {}
            request.session.modified = True
        
        return redirect('menus')
    
def revisar_pedidos(request):
    pedidos = Pedido.objects.filter(user=request.user).prefetch_related('items')
    return render(request, 'pedidos.html', {'pedidos': pedidos})