from django.shortcuts import render
from rest_framework import viewsets
from .models import Pedido, Pedido_menu
from .serializer import Pedido_menuSerializer, PedidoSerializer  

# Create your views here.
class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class Pedido_menuViewSet(viewsets.ModelViewSet):
    queryset = Pedido_menu.objects.all()
    serializer_class = Pedido_menuSerializer

