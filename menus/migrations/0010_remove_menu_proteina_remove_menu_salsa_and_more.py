# Generated by Django 4.2.11 on 2024-06-07 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0009_alter_menu_proteina_alter_menu_salsa_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='proteina',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='salsa',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='vegetal1',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='vegetal2',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='vegetal3',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='vegetal4',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='vegetal5',
        ),
    ]
