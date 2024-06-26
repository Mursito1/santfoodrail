# Generated by Django 4.2.11 on 2024-05-15 21:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('menus', '0003_menu_descripcion_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pedido', models.CharField(max_length=50)),
                ('total', models.PositiveIntegerField()),
                ('ganancia_total', models.PositiveIntegerField()),
                ('nombre_cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido_menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_menu', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='menus.menu')),
                ('id_pedido', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pedidos.pedido')),
            ],
        ),
    ]
