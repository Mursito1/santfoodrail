from rest_framework import serializers
from .models import Contacto, Estado_contacto, Tipo_contacto

class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = '__all__'

class Tipo_contactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_contacto
        fields = '__all__'

class Estado_contactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado_contacto
        fields = '__all__'