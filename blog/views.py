from django.shortcuts import render, redirect, get_object_or_404
from contactos.forms import ContactoAdminForm, ContactoForm
from contactos.models import Contacto, Estado_contacto, Tipo_contacto
from menus.carrito import Carrito
from pedidos.models import Pedido, PedidoItem
from .forms import CustomUserCreationForm, MenuForm, ProteinaForm, SalsaForm, UserForm, VegetalForm
from menus.models import Menu, Proteina, Salsa, Vegetal
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST


# Create your views here.
def render_articles(request):
    menus = Menu.objects.all()
    return render(request, 'index.html', {'menus': menus})

def nosotros(request):
    return render(request, 'nosotros.html')

def crud(request):
    contactos = Contacto.objects.all()
    estados_contacto = Estado_contacto.objects.all()
    tipos_contacto = Tipo_contacto.objects.all()

    estado_filter = request.GET.get('estado_contacto')
    if estado_filter:
        contactos = contactos.filter(estado_contacto__id=estado_filter)

    tipo_filter = request.GET.get('tipo_contacto')
    if tipo_filter:
        contactos = contactos.filter(tipo_contacto__id=tipo_filter)

    if request.method == 'POST':
        contacto_id = request.POST.get('contacto_id')
        contacto = get_object_or_404(Contacto, pk=contacto_id) if contacto_id else None

        form = ContactoAdminForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            messages.success(request, 'El contacto se ha editado exitosamente.')
            return redirect('crud')
    else:
        form = ContactoAdminForm()

    return render(request, 'crud.html', {
        'contactos': contactos,
        'estados_contacto': estados_contacto,
        'tipos_contacto': tipos_contacto,
        'form': form
    })


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

#-----------------------------------------------------------------------------------------------------------
# RECUPERAR CONTRASEÑ



@login_required
def editar_usuario(request):
    user = request.user
    
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('perfil') 
    else:
        form = UserForm(instance=user)
    
    return render(request, 'editar_usuario.html', {'form': form})

def perfil(request):
    return render(request, 'perfil.html')

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

#-------------------------------------------------------------------------------
#IMPLEMENTACION DEL CARRITO DE COMPRAS CON AJAX

def is_ajax(request):
    return request.headers.get('x-requested-with') == 'XMLHttpRequest'

def agregar_menu(request, menu_id):
     carrito = Carrito(request)
     menu = get_object_or_404(Menu, id=menu_id)
     if request.method == 'POST':
         proteina_id = request.POST.get('proteina')
         vegetales_ids = request.POST.getlist('vegetales')
         salsas_ids = request.POST.getlist('salsas')
         ingredientes = {
             'proteina': proteina_id,
             'vegetales': vegetales_ids,
             'salsas': salsas_ids
         }
         carrito.agregar(menu, ingredientes)
         if is_ajax(request):
             return JsonResponse({'success': True, 'total': carrito.total(), 'items': carrito.carrito})
         return redirect("menus")
     return redirect("menus")

def eliminar_menu(request, menu_id):
     carrito = Carrito(request)
     carrito.eliminar(menu_id)
     if is_ajax(request):
         return JsonResponse({'success': True, 'total': carrito.total(), 'items': carrito.carrito})
     return redirect("menus")

def restar_menu(request, menu_id):
     carrito = Carrito(request)
     carrito.restar(menu_id)
     if is_ajax(request):
         return JsonResponse({'success': True, 'total': carrito.total(), 'items': carrito.carrito})
     return redirect("menus")

def limpiar_carrito(request):
     carrito = Carrito(request)
     carrito.limpiar()
     if is_ajax(request):
         return JsonResponse({'success': True, 'total': carrito.total(), 'items': carrito.carrito})
     return redirect("menus")

def agregar_producto(request):
    data = {
        'form': MenuForm()
    }
    if request.method == 'POST':
        formulario = MenuForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se ha guardado correctamente")
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
            pedido = Pedido.objects.create(user=request.user)
            for item in carrito.values():
                PedidoItem.objects.create(
                    pedido=pedido,
                    menu_id=item["menu_id"],
                    nombre=item["nombre"],
                    precio=item["acumulado"],
                    cantidad=item["cantidad"],
                )

                menu = Menu.objects.get(id=item["menu_id"])
                menu.stock -= item["cantidad"]
                menu.save()

            request.session["carrito"] = {}
            request.session.modified = True

            messages.success(request, "Tu pedido ha sido realizado con éxito.")
        return redirect('menus')
    
def revisar_pedidos(request):
    pedidos = Pedido.objects.filter(user=request.user).prefetch_related('items')
    return render(request, 'pedidos.html', {'pedidos': pedidos})

def detalle_menu(request, menu_id):
    menu = get_object_or_404(Menu, pk=menu_id)
    return render(request, 'detalle.html', {'menu': menu})

def agregar_proteina(request):
    data = {
        'form': ProteinaForm()
    }

    if request.method == 'POST':
        formulario = ProteinaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se ha guardado correctamente")
        else:
            data["form"] = formulario
    return render(request, 'administracion/agregar_proteina.html', data)

def agregar_salsa(request):
    data = {
        'form': SalsaForm()
    }

    if request.method == 'POST':
        formulario = SalsaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se ha guardado correctamente")
        else:
            data["form"] = formulario
    return render(request, 'administracion/agregar_salsa.html', data)

def agregar_vegetal(request):
    data = {
        'form': VegetalForm()
    }

    if request.method == 'POST':
        formulario = VegetalForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se ha guardado correctamente")
        else:
            data["form"] = formulario
    return render(request, 'administracion/agregar_vegetal.html', data)

def lista_ingredientes(request):
    proteinas = Proteina.objects.all()
    vegetales = Vegetal.objects.all()
    salsas = Salsa.objects.all()

    proteina_filtrada = request.GET.get('proteina')
    if proteina_filtrada:
        proteinas = proteinas.filter(nombre__icontains=proteina_filtrada)
    
    vegetal_filtrado = request.GET.get('vegetal')
    if vegetal_filtrado:
        vegetales = vegetales.filter(nombre__icontains=vegetal_filtrado)
    
    salsa_filtrada = request.GET.get('salsa')
    if salsa_filtrada:
        salsas = salsas.filter(nombre__icontains=salsa_filtrada)

    context = {
        'proteinas': proteinas,
        'vegetales': vegetales,
        'salsas': salsas,
    }
    return render(request, 'lista_ingredientes.html', context)

def eliminar_proteina(request, id):
    proteina = get_object_or_404(Proteina, id=id)
    if request.method == 'POST':
        proteina.delete()
        messages.success(request, 'Proteína eliminada correctamente.')
        return redirect('lista_ingredientes')
    return render(request, 'confirmar_eliminacion.html', {'objeto': proteina})

def eliminar_vegetal(request, id):
    vegetal = get_object_or_404(Vegetal, id=id)
    if request.method == 'POST':
        vegetal.delete()
        messages.success(request, 'Vegetal eliminado correctamente.')
        return redirect('lista_ingredientes')
    return render(request, 'confirmar_eliminacion.html', {'objeto': vegetal})

def eliminar_salsa(request, id):
    salsa = get_object_or_404(Salsa, id=id)
    if request.method == 'POST':
        salsa.delete()
        messages.success(request, 'Salsa eliminada correctamente.')
        return redirect('lista_ingredientes')
    return render(request, 'confirmar_eliminacion.html', {'objeto': salsa})

def editar_proteina(request, id):
    proteina = get_object_or_404(Proteina, id=id)
    if request.method == 'POST':
        form = ProteinaForm(request.POST, instance=proteina)
        if form.is_valid():
            form.save()
            messages.success(request, 'Proteína editada correctamente.')
            return redirect('lista_ingredientes')
    else:
        form = ProteinaForm(instance=proteina)
    return render(request, 'administracion/editar_ingrediente.html', {'form': form, 'tipo_ingrediente': 'proteina'})

def editar_vegetal(request, id):
    vegetal = get_object_or_404(Vegetal, id=id)
    if request.method == 'POST':
        form = VegetalForm(request.POST, instance=vegetal)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vegetal editado correctamente.')
            return redirect('lista_ingredientes')
    else:
        form = VegetalForm(instance=vegetal)
    return render(request, 'administracion/editar_ingrediente.html', {'form': form, 'tipo_ingrediente': 'vegetal'})

def editar_salsa(request, id):
    salsa = get_object_or_404(Salsa, id=id)
    if request.method == 'POST':
        form = SalsaForm(request.POST, instance=salsa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Salsa editada correctamente.')
            return redirect('lista_ingredientes')
    else:
        form = SalsaForm(instance=salsa)
    return render(request, 'administracion/editar_ingrediente.html', {'form': form, 'tipo_ingrediente': 'salsa'})



