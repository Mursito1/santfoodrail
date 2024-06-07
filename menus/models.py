from django.db import models


# Create your models here.

class Ingrediente(models.Model):
    nombre_ingrediente = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_ingrediente

class Calificacion(models.Model):
    calificacion = models.IntegerField()

    def __str__(self):
        return self.calificacion

class Proteina(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class Vegetal(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class Salsa(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Menu(models.Model):
    nombre_menu = models.CharField(max_length=50)
    precio = models.PositiveIntegerField()
    ganancia = models.PositiveIntegerField()
    estado_menu = models.BooleanField()
    descripcion_menu = models.CharField(max_length=300)
    imagen = models.ImageField(upload_to='images/')
    proteina = models.ManyToManyField(Proteina)
    vegetal = models.ManyToManyField(Vegetal)
    salsa = models.ManyToManyField(Salsa)

    def __str__(self):
        return self.nombre_menu
    
class Calificacion_Menu(models.Model):
    id_menu = models.ForeignKey(Menu, on_delete=models.PROTECT)
    id_calificacion = models.ForeignKey(Calificacion, on_delete=models.PROTECT, null=True)

    def int(self):
        return self.id

    

    
