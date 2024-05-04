from django.shortcuts import render
from rest_framework import viewsets
from .models import Contacto, Estado_contacto, Tipo_contacto
from .serializer import ContactoSerializer, Estado_contactoSerializer, Tipo_contactoSerializer

# Create your views here.
class ContactoViewSet(viewsets.ModelViewSet):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer

class Tipo_contactoViewSet(viewsets.ModelViewSet):
    queryset = Tipo_contacto.objects.all()
    serializer_class = Tipo_contactoSerializer

class Estado_contactoViewSet(viewsets.ModelViewSet):
    queryset = Estado_contacto.objects.all()
    serializer_class = Estado_contactoSerializer

