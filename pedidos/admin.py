from django.contrib import admin

from pedidos.models import Pedido, Pedido_menu

# Register your models here.

admin.site.register(Pedido)
admin.site.register(Pedido_menu)