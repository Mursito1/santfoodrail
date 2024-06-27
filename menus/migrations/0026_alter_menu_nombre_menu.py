# Generated by Django 4.2.11 on 2024-06-19 23:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0025_alter_menu_descripcion_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='nombre_menu',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(8), django.core.validators.RegexValidator(code='invalid_nombre_menu', message='El nombre del menú debe comenzar con una letra mayúscula y solo puede contener letras y espacios.', regex='^(?!^[.\\s]*$)[a-zA-Z0-9áéíóúÁÉÍÓÚ.,\\s]+$')]),
        ),
    ]