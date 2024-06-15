from django.db import models
from django.core.validators import MinValueValidator, RegexValidator, MinLengthValidator, EmailValidator

# Create your models here.

class Tipo_contacto(models.Model):
    tipo_contacto = models.CharField(
        max_length=20,
        validators=[
            MinLengthValidator(3),
            RegexValidator(
                regex='^[a-zA-Z]+$',
                message='El tipo de contacto solo puede contener letras y debe ser mayor a 3 letras'
            ),
        ]
    )

    def __str__(self):
        return self.tipo_contacto
    
class Estado_contacto(models.Model):
    estado_contacto = models.CharField(max_length=50)

    def __str__(self):
        return self.estado_contacto

class Contacto(models.Model):
    nombre = models.CharField(
        max_length=100,  
        validators=[
            RegexValidator(
                regex='^[a-zA-Z]+$',
                message='El nombre solo puede contener letras',
                code='invalid_nombre'
            )
        ]
    )
    correo = models.EmailField(
        validators=[
            EmailValidator(
                message='Introduzca una dirección de correo electrónico válida',
                code='invalid_correo'
            )
        ]
    )
    tipo_contacto = models.ForeignKey(Tipo_contacto, on_delete=models.PROTECT)
    mensaje_contacto = models.CharField(
        max_length=300,
        validators=[
            MinLengthValidator(10),
            RegexValidator(
                regex='^(?!.*[^a-zA-Z. ])[a-zA-Z]+(?:[a-zA-Z. ]*[a-zA-Z]+)*$',
                message='El mensaje solo puede contener letras y puntos. Además, no pueden ser solo puntos.',
                code='invalid_mensaje_contacto'
            )
        ]
    )
    estado_contacto = models.ForeignKey(Estado_contacto, on_delete=models.SET_DEFAULT, default=1, blank=True, null=True)
    respuesta = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nombre