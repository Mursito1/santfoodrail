from django.shortcuts import render
from rest_framework import viewsets
from .models import Calificacion, Calificacion_Menu, Ingrediente, Menu, Ingrediente_menu
from .serializer import Calificacion_MenuSerializer, CalificacionSerializer, Ingrediente_menuSerializer, IngredienteSerializer, MenuSerializer

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

class CalificacionViewSet(viewsets.ModelViewSet):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer

class Calificacion_MenuViewSet(viewsets.ModelViewSet):
    queryset = Calificacion_Menu.objects.all()
    serializer_class = Calificacion_MenuSerializer

    