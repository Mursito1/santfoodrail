from django.shortcuts import render

from menus.models import Menu

# Create your views here.
def render_articles(request):
    return render(request, 'index.html')

def contacto(request):
    return render(request, 'contacto.html')

def login(request):
    return render(request, 'login.html')

def menus(request):
    return render(request, 'menus.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def registro(request):
    return render(request, 'registro.html')

def menus(request):
    menus = Menu.objects.all()
    return render(request, 'menus.html', {'menus': menus})
