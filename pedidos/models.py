from django.db import models
from django.contrib.auth.models import User
from menus.models import Menu

# Create your models here.

class Pedido(models.Model):
    nombre_cliente = models.ForeignKey(User, on_delete=models.PROTECT)
    fecha_pedido = models.CharField(max_length=50)
    total = models.PositiveIntegerField()
    ganancia_total = models.PositiveIntegerField()

    def int(self):
        return self.nombre_cliente
    
class Pedido_menu(models.Model):
    id_menu = models.ForeignKey(Menu, on_delete=models.PROTECT)
    id_pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)

    def int(self):
        return self.id_pedido
