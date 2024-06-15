from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, RegexValidator, MinLengthValidator


# Create your models here.

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
    nombre_menu = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(8),
            RegexValidator(
                regex='^[a-zA-Z]+$',
                message='El nombre del menú solo puede contener letras.',
                code='invalid_nombre_menu'
            )
        ]
    )
    precio = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    ganancia = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    estado_menu = models.BooleanField()
    descripcion_menu = models.CharField(
        max_length=300,
        validators=[
            MinLengthValidator(10),
            RegexValidator(
                regex='^(?!.*[^a-zA-Z. ])[a-zA-Z]+(?:[a-zA-Z. ]*[a-zA-Z]+)*$',
                message='La descripción solo puede contener letras y puntos. Además, no pueden ser solo puntos.',
                code='invalid_descripcion_menu'
            )
        ]
    )
    imagen = models.ImageField(upload_to='images/')
    proteina = models.ManyToManyField(Proteina)
    vegetal = models.ManyToManyField(Vegetal)
    salsa = models.ManyToManyField(Salsa)

    def __str__(self):
        return self.nombre_menu

    def clean(self):
        super().clean()

        if not self.descripcion_menu or len(self.descripcion_menu) < 10:
            raise ValidationError({
                'descripcion_menu': 'La descripción debe tener al menos 10 caracteres.'
            })
    
class Calificacion_Menu(models.Model):
    id_menu = models.ForeignKey(Menu, on_delete=models.PROTECT)
    id_calificacion = models.ForeignKey(Calificacion, on_delete=models.PROTECT, null=True)

    def int(self):
        return self.id

    

    
