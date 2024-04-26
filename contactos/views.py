from django.shortcuts import render
from rest_framework import viewsets
from .models import Contacto
from .serializer import ContactoSerializer

# Create your views here.
class ContactoViewSet(viewsets.ModelViewSet):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer