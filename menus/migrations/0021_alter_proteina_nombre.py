# Generated by Django 4.2.11 on 2024-06-19 22:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0020_alter_proteina_nombre_alter_salsa_nombre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proteina',
            name='nombre',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.RegexValidator(message='El nombre de la proteina solo puede contener letras y debe ser mayor a 3 letras', regex='^[a-zA-Z ]+$')]),
        ),
    ]