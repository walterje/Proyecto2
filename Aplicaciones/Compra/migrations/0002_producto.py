# Generated by Django 3.1.5 on 2021-03-12 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Compra', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('cod_producto', models.IntegerField(primary_key=True, serialize=False, verbose_name='Codigo Producto')),
                ('tipo_producto', models.CharField(choices=[('1', 'Producto'), ('2', 'Servicio')], default='1', max_length=2)),
                ('nombre_producto', models.CharField(max_length=50, unique=True, verbose_name='producto')),
                ('descripcion', models.CharField(blank=True, max_length=30)),
                ('marca', models.CharField(max_length=30)),
                ('cant_stock', models.IntegerField()),
                ('cant_minima_stock', models.IntegerField(default=1)),
                ('estado', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'producto',
            },
        ),
    ]