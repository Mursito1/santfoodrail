# Generated by Django 4.2.11 on 2024-06-18 20:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0017_alter_proteina_nombre_alter_salsa_nombre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='descripcion_menu',
            field=models.CharField(max_length=300, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.RegexValidator(code='invalid_descripcion_menu', message='La descripción solo puede contener letras, puntos y espacios. No puede estar compuesta solo por puntos o espacios.', regex='^(?!^[. ]*$)[a-zA-Z. ]+$')]),
        ),
        migrations.AlterField(
            model_name='menu',
            name='nombre_menu',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(8), django.core.validators.RegexValidator(code='invalid_nombre_menu', message='El nombre del menú debe comenzar con una letra mayúscula y solo puede contener letras y espacios.', regex='^[A-Z][a-zA-Z ]+$')]),
        ),
    ]
