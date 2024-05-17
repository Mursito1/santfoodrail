from django.shortcuts import render
from rest_framework import viewsets
from .models import Ingrediente, Menu, Ingrediente_menu
from .serializer import Ingrediente_menuSerializer, IngredienteSerializer, MenuSerializer

# Create your views here.
class IngredienteViewSet(viewsets.ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class Ingrediente_menuViewSet(viewsets.ModelViewSet):
    queryset = Ingrediente_menu.objects.all()
    serializer_class = Ingrediente_menuSerializer
