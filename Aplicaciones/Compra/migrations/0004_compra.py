# Generated by Django 3.1.5 on 2021-03-12 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Referenciales', '0004_tipodocumento'),
        ('Compra', '0003_detalllepreciocompra'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('nro_factura', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='Numero Factura')),
                ('tipo_compra', models.CharField(max_length=10)),
                ('fecha_emision', models.DateField(auto_now=True)),
                ('condicion', models.CharField(choices=[('0', 'Contado'), ('1', 'Credito')], default='0', max_length=2)),
                ('total_IVA', models.FloatField()),
                ('total_descuento', models.FloatField()),
                ('total_importe', models.FloatField()),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Referenciales.empleado')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Compra.proveedor')),
                ('tipo_documento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Referenciales.tipodocumento')),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras',
                'db_table': 'compra',
                'ordering': ['nro_factura'],
            },
        ),
    ]
