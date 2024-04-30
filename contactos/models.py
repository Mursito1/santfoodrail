from django.db import models

# Create your models here.

class Tipo_contacto(models.Model):
    tipo_contacto = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo_contacto
    
class Estado_contacto(models.Model):
    estado_contacto = models.CharField(max_length=50)

    def __str__(self):
        return self.estado_contacto

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    tipo_contacto = models.ForeignKey(Tipo_contacto, on_delete=models.PROTECT)
    mensaje = models.TextField()
    estado_contacto = models.ForeignKey(Estado_contacto, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.title