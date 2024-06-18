from django.shortcuts import render, redirect, get_object_or_404
from contactos.forms import ContactoAdminForm, ContactoForm
from contactos.models import Contacto, Estado_contacto, Tipo_contacto
from menus.carrito import Carrito
from pedidos.models import Pedido, PedidoItem
from .forms import CustomUserCreationForm, MenuForm
from menus.models import Menu
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
        form = ContactoAdminForm(request.POST)
        if form.is_valid():
            contacto = form.save(commit=False)
            if contacto.respuesta:
                contacto.estado_contacto_id = 3
            else:
                contacto.estado_contacto_id = 2
            contacto.save() 
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


@require_POST
def agregar_menu(request, menu_id):
    carrito = Carrito(request)
    menu = get_object_or_404(Menu, id=menu_id)
    
    proteina_id = request.POST.get('proteina')
    vegetales_ids = request.POST.getlist('vegetales')
    salsas_ids = request.POST.getlist('salsas')
    ingredientes = {
        'proteina': proteina_id,
        'vegetales': vegetales_ids,
        'salsas': salsas_ids
    }
    
    carrito.agregar(menu, ingredientes)
    
    if request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        items = [{
            'menu_id': item['menu_id'],
            'nombre': item['nombre'],
            'acumulado': item['acumulado'],
            'cantidad': item['cantidad'],
            'imagen': item['imagen'].url if item['imagen'] else '',  # Obtener la URL de la imagen, si existe
        } for item in carrito.carrito.values()]
        return JsonResponse({'success': True, 'total': carrito.total(), 'items': items})
    
    return redirect('menus')

def eliminar_menu(request, menu_id):
    carrito = Carrito(request)
    carrito.eliminar(menu_id)
    if is_ajax(request):
        items = [{
            'menu_id': item['menu_id'],
            'nombre': item['nombre'],
            'acumulado': item['acumulado'],
            'cantidad': item['cantidad'],
            'imagen': item['imagen_url'],  # Usar la URL de la imagen almacenada en el carrito
        } for item in carrito.carrito.values()]
        return JsonResponse({'success': True, 'total': carrito.total(), 'items': items})
    return redirect("menus")

def restar_menu(request, menu_id):
    carrito = Carrito(request)
    carrito.restar(menu_id)
    if is_ajax(request):
        items = [{
            'menu_id': item['menu_id'],
            'nombre': item['nombre'],
            'acumulado': item['acumulado'],
            'cantidad': item['cantidad'],
            'imagen': item['imagen_url'],  # Usar la URL de la imagen almacenada en el carrito
        } for item in carrito.carrito.values()]
        return JsonResponse({'success': True, 'total': carrito.total(), 'items': items})
    return redirect("menus")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    if is_ajax(request):
        return JsonResponse({'success': True, 'total': carrito.total(), 'items': carrito.carrito})
    return redirect("menus")


#AGREGAR MENU PERO SIN IMAGEN
# def agregar_menu(request, menu_id):
#     carrito = Carrito(request)
#     menu = get_object_or_404(Menu, id=menu_id)
#     if request.method == 'POST':
#         proteina_id = request.POST.get('proteina')
#         vegetales_ids = request.POST.getlist('vegetales')
#         salsas_ids = request.POST.getlist('salsas')
#         ingredientes = {
#             'proteina': proteina_id,
#             'vegetales': vegetales_ids,
#             'salsas': salsas_ids
#         }
#         carrito.agregar(menu, ingredientes)
#         if is_ajax(request):
#             return JsonResponse({'success': True, 'total': carrito.total(), 'items': carrito.carrito})
#         return redirect("menus")
#     return redirect("menus")

# def eliminar_menu(request, menu_id):
#     carrito = Carrito(request)
#     carrito.eliminar(menu_id)
#     if is_ajax(request):
#         return JsonResponse({'success': True, 'total': carrito.total(), 'items': carrito.carrito})
#     return redirect("menus")

# def restar_menu(request, menu_id):
#     carrito = Carrito(request)
#     carrito.restar(menu_id)
#     if is_ajax(request):
#         return JsonResponse({'success': True, 'total': carrito.total(), 'items': carrito.carrito})
#     return redirect("menus")

# def limpiar_carrito(request):
#     carrito = Carrito(request)
#     carrito.limpiar()
#     if is_ajax(request):
#         return JsonResponse({'success': True, 'total': carrito.total(), 'items': carrito.carrito})
#     return redirect("menus")



# def agregar_menu(request, menu_id):
#     if request.method == 'POST':
#         carrito = Carrito(request)
#         menu = Menu.objects.get(id=menu_id)
#         proteina_id = request.POST.get('proteina')
#         vegetales_ids = request.POST.getlist('vegetales')
#         salsas_ids = request.POST.getlist('salsas')
#         ingredientes = {
#             'proteina': proteina_id,
#             'vegetales': vegetales_ids,
#             'salsas': salsas_ids
#         }
#         carrito.agregar(menu, ingredientes)
#         return redirect("menus")
#     else:
#         return redirect("menus")

# def eliminar_menu(request, menu_id):
#     carrito = Carrito(request)
#     menu = Menu.objects.get(id=menu_id)
#     carrito.eliminar(menu)
#     return redirect("menus")

# def restar_menu(request, menu_id):
#     carrito = Carrito(request)
#     menu = Menu.objects.get(id=menu_id)
#     carrito.restar(menu)
#     return redirect("menus")

# def limpiar_carrito(request):
#     carrito = Carrito(request)
#     carrito.limpiar()
#     return redirect("menus")

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
            pedido = Pedido.objects.create(user=request.user)
            for item in carrito.values():
                PedidoItem.objects.create(
                    pedido=pedido,
                    menu_id=item["menu_id"],
                    nombre=item["nombre"],
                    precio=item["acumulado"],
                    cantidad=item["cantidad"],
                )

            request.session["carrito"] = {}
            request.session.modified = True
        
        return redirect('menus')
    
def revisar_pedidos(request):
    pedidos = Pedido.objects.filter(user=request.user).prefetch_related('items')
    return render(request, 'pedidos.html', {'pedidos': pedidos})

def detalle_menu(request, menu_id):
    menu = get_object_or_404(Menu, pk=menu_id)
    return render(request, 'detalle.html', {'menu': menu})


