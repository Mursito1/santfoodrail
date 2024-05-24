# Generated by Django 4.2.11 on 2024-05-24 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0004_calificacion_menu_calificacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='calificacion',
        ),
        migrations.CreateModel(
            name='Calificacion_Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_calificacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='menus.calificacion')),
                ('id_menu', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='menus.menu')),
            ],
        ),
    ]
