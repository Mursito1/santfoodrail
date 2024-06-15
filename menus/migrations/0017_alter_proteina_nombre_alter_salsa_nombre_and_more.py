# Generated by Django 4.2.11 on 2024-06-15 05:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0016_alter_menu_descripcion_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proteina',
            name='nombre',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.RegexValidator(message='El nombre de la proteina solo puede contener letras y debe ser mayor a 3 letras', regex='^[a-zA-Z]+$')]),
        ),
        migrations.AlterField(
            model_name='salsa',
            name='nombre',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.RegexValidator(message='El nombre de la salsa solo puede contener letras y debe ser mayor a 3 letras', regex='^[a-zA-Z]+$')]),
        ),
        migrations.AlterField(
            model_name='vegetal',
            name='nombre',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.RegexValidator(message='El nombre del vegetal solo puede contener letras y debe ser mayor a 3 letras', regex='^[a-zA-Z]+$')]),
        ),
    ]
