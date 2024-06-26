# Generated by Django 4.2.11 on 2024-06-18 21:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0018_alter_menu_descripcion_menu_alter_menu_nombre_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='descripcion_menu',
            field=models.CharField(max_length=300, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.RegexValidator(code='invalid_descripcion_menu', message='La descripción solo puede contener letras, puntos y espacios. No puede estar compuesta solo por puntos o espacios.', regex='^(?!^[. ]*$)[a-zA-Z., ]+$')]),
        ),
    ]
