# Generated by Django 4.2.11 on 2024-06-28 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0028_remove_calificacion_menu_id_calificacion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='stock',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
