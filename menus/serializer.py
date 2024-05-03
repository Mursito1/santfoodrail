from rest_framework import serializers
from .models import Ingrediente, Menu, Ingrediente_menu

class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class Ingrediente_menuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente_menu
        fields = '__all__'
