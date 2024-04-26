from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)
    contraseña = models.CharField(max_length=200)
    comuna = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)

    
    def __str__(self):
        return self.title