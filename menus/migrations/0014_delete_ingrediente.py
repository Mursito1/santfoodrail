# Generated by Django 4.2.11 on 2024-06-14 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0013_alter_menu_descripcion_menu_alter_menu_nombre_menu'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Ingrediente',
        ),
    ]
