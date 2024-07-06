from django.db import models
from django.core.validators import MinValueValidator, RegexValidator, MinLengthValidator, EmailValidator
from django.db import models
from django.core.validators import (
    MinLengthValidator,
    RegexValidator,
    EmailValidator,
    ValidationError,
)
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError as DjangoValidationError

# Create your models here.


class Tipo_contacto(models.Model):
    tipo_contacto = models.CharField(
        max_length=20,
        validators=[
            MinLengthValidator(3),
            RegexValidator(
                regex='^[a-zA-ZñÑ]+$',
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



def validate_unique_chars(value):
    previous_char = ''
    for char in value:
        if char == previous_char:
            raise ValidationError(
                _('El campo no puede contener caracteres repetidos consecutivos.'),
                code='invalid'
            )
        previous_char = char
        
def validate_message_sense(value):
    if len(set(value.lower())) < 10:
        raise ValidationError(
            _('El mensaje debe contener al menos 10 caracteres diferentes.'),
            code='invalid'
        )

class Contacto(models.Model):
    nombre = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(3, message='El nombre debe tener al menos 3 caracteres'),
            RegexValidator(
                regex=r'^[a-zA-ZñÑ]+$',
                message='El nombre solo puede contener letras',
                code='invalid_nombre'
            ),
            validate_unique_chars
        ]
    )
    correo = models.EmailField(
    validators=[
        EmailValidator(message='Introduzca una dirección de correo electrónico válida'),
        RegexValidator(
            regex=r'^[^@]+@[a-zA-Z0-9.]{5,}\.[a-zA-Z]{2,4}$',
            message='El correo debe tener al menos 5 caracteres después del "@" y terminar en ".cl" o ".com"',
            code='invalid_correo'
            )
        ]
    )

    
    
    tipo_contacto = models.ForeignKey(Tipo_contacto, on_delete=models.PROTECT)
    mensaje_contacto = models.CharField(
        max_length=300,
        validators=[
            MinLengthValidator(10, message='El mensaje debe tener al menos 10 caracteres'),
            RegexValidator(
                regex=r'^(?!.*([^a-zA-Z. ñÑáéíóúÁÉÍÓÚ])).*$',
                message='El mensaje solo puede contener letras y puntos. Además, no pueden ser solo puntos.',
                code='invalid_mensaje_contacto'
            ),
            validate_unique_chars,
            validate_message_sense
        ]
    )
    estado_contacto = models.ForeignKey(Estado_contacto, on_delete=models.SET_DEFAULT, default=1, blank=True, null=True)
    respuesta = models.TextField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.nombre.strip():
            raise DjangoValidationError(_('El nombre no puede estar vacío o contener solo espacios en blanco.'))
        if not self.correo.strip():
            raise DjangoValidationError(_('El correo no puede estar vacío o contener solo espacios en blanco.'))
        if not self.mensaje_contacto.strip():
            raise DjangoValidationError(_('El mensaje no puede estar vacío o contener solo espacios en blanco.'))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre

