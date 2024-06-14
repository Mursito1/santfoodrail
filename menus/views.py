from django.shortcuts import render
from rest_framework import viewsets
from .models import Calificacion, Calificacion_Menu, Menu
from .serializer import Calificacion_MenuSerializer, CalificacionSerializer, MenuSerializer

# Create your views here.

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class CalificacionViewSet(viewsets.ModelViewSet):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer

class Calificacion_MenuViewSet(viewsets.ModelViewSet):
    queryset = Calificacion_Menu.objects.all()
    serializer_class = Calificacion_MenuSerializer

    