# Generated by Django 4.2.11 on 2024-06-25 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0027_alter_categoria_nombre_alter_menu_descripcion_menu_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calificacion_menu',
            name='id_calificacion',
        ),
        migrations.RemoveField(
            model_name='calificacion_menu',
            name='id_menu',
        ),
        migrations.DeleteModel(
            name='Calificacion',
        ),
        migrations.DeleteModel(
            name='Calificacion_Menu',
        ),
    ]
