from django.db import models


# Create your models here.

class Ingrediente(models.Model):
    nombre_ingrediente = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_ingrediente

class Menu(models.Model):
    nombre_menu = models.CharField(max_length=50)
    precio = models.PositiveIntegerField()
    ganancia = models.PositiveIntegerField()
    estado_menu = models.BooleanField()
    imagen = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.nombre_menu

class Ingrediente_menu(models.Model):
    id_ingrediente = models.ForeignKey(Ingrediente, on_delete=models.PROTECT)
    id_menu = models.ForeignKey(Menu, on_delete=models.PROTECT)

    def int(self):
        return self.id
    