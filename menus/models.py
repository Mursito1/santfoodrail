from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, RegexValidator, MinLengthValidator


# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(3),
            RegexValidator(
                regex='^[a-zA-ZñÑ ]+$',
                message='El nombre de la categoria solo puede contener letras y debe ser mayor a 3 letras'
            ),
        ]
    )

    def __str__(self):
        return self.nombre

class Proteina(models.Model):
    nombre = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(3),
            RegexValidator(
                regex='^[a-zA-ZñÑ ]+$',
                message='El nombre de la proteina solo puede contener letras y debe ser mayor a 3 letras'
            ),
        ]
    )

    def __str__(self):
        return self.nombre
    
class Vegetal(models.Model):
    nombre = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(3),
            RegexValidator(
                regex='^[a-zA-ZñÑ ]+$',
                message='El nombre del vegetal solo puede contener letras y debe ser mayor a 3 letras'
            ),
        ]
    )

    def __str__(self):
        return self.nombre
    
class Salsa(models.Model):
    nombre = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(3),
            RegexValidator(
                regex='^[a-zA-ZñÑ ]+$',
                message='El nombre de la salsa solo puede contener letras y debe ser mayor a 3 letras'
            ),
        ]
    )

    def __str__(self):
        return self.nombre


class Menu(models.Model):
    nombre_menu = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(8),
            RegexValidator(
                regex='^[A-ZÑ][a-zA-ZñÑ ]+$',
                message='El nombre del menú debe comenzar con una letra mayúscula y solo puede contener letras y espacios.',
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
                regex=r'^(?!^[.\s]*$)[a-zA-Z0-9áéíóúñÑÁÉÍÓÚ.,\s]+$',
                message='La descripción solo puede contener letras, números, puntos y espacios. No puede estar compuesta solo por puntos o espacios.',
                code='invalid_descripcion_menu'
            )
        ]
    )
    imagen = models.ImageField(upload_to='images/')
    proteina = models.ManyToManyField(Proteina)
    vegetal = models.ManyToManyField(Vegetal)
    salsa = models.ManyToManyField(Salsa)
    categoria = models.ManyToManyField(Categoria)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre_menu

    def clean(self):
        super().clean()

        if not self.descripcion_menu or len(self.descripcion_menu) < 10:
            raise ValidationError({
                'descripcion_menu': 'La descripción debe tener al menos 10 caracteres.'
            })


    

    
