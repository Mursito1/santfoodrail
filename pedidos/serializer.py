from rest_framework import serializers
from .models import Pedido, Pedido_Menu

class Pedido_MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido_Menu
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'