# Generated by Django 4.2.11 on 2024-05-04 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0005_rename_mensaje_contacto_mensaje_contacto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='correo',
            field=models.EmailField(max_length=254),
        ),
    ]
