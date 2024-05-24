from django.shortcuts import render
from rest_framework import viewsets
from .models import Pedido, Pedido_Menu
from .serializer import Pedido_MenuSerializer, PedidoSerializer  

# Create your views here.
class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class Pedido_MenuViewSet(viewsets.ModelViewSet):
    queryset = Pedido_Menu.objects.all()
    serializer_class = Pedido_MenuSerializer

