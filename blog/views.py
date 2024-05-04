from django.shortcuts import render
from contactos.forms import ContactoForm
from menus.models import Menu

# Create your views here.
def render_articles(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def registro(request):
    return render(request, 'registro.html')

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


