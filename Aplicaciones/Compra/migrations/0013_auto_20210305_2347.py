# Generated by Django 3.1.5 on 2021-03-06 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Compra', '0012_auto_20210223_2307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='cod_tipo',
        ),
        migrations.AddField(
            model_name='producto',
            name='tipo_producto',
            field=models.IntegerField(choices=[('1', 'Producto'), ('2', 'Servicio')], default='1'),
        ),
        migrations.AlterField(
            model_name='pedidos_compra',
            name='descripcion_pedido',
            field=models.CharField(blank=True, max_length=50, verbose_name='Pedido_compra'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.DeleteModel(
            name='Tipo_producto',
        ),
    ]