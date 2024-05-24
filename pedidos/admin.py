from django.contrib import admin

from pedidos.models import Pedido, Pedido_Menu

# Register your models here.

admin.site.register(Pedido)
admin.site.register(Pedido_Menu)