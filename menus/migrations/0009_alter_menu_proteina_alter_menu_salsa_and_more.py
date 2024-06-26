# Generated by Django 4.2.11 on 2024-06-06 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0008_rename_nombre_salsa_salsa_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='proteina',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='menus.proteina'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='salsa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='menus.salsa'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='vegetal1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='menus.vegetal1'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='vegetal2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='menus.vegetal2'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='vegetal3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='menus.vegetal3'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='vegetal4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='menus.vegetal4'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='vegetal5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='menus.vegetal5'),
        ),
    ]
