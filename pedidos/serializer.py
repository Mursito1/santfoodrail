from rest_framework import serializers
from .models import Pedido, Pedido_menu

class Pedido_menuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido_menu
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'