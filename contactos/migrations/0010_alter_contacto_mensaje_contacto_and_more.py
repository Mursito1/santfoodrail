# Generated by Django 4.2.11 on 2024-06-22 04:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0009_contacto_respuesta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='mensaje_contacto',
            field=models.CharField(max_length=300, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.RegexValidator(code='invalid_mensaje_contacto', message='El mensaje solo puede contener letras y puntos. Además, no pueden ser solo puntos.', regex='^(?!.*[^a-zA-Z. ñÑáéíóúÁÉÍÓÚ])[a-zA-Z]+(?:[a-zA-Z. ñÑáéíóúÁÉÍÓÚ]*[a-zA-Z]+)*$')]),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='nombre',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(code='invalid_nombre', message='El nombre solo puede contener letras', regex='^[a-zA-ZñÑ]+$')]),
        ),
        migrations.AlterField(
            model_name='tipo_contacto',
            name='tipo_contacto',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.RegexValidator(message='El tipo de contacto solo puede contener letras y debe ser mayor a 3 letras', regex='^[a-zA-ZñÑ]+$')]),
        ),
    ]