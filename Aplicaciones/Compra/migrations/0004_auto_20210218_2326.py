# Generated by Django 3.1.5 on 2021-02-19 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Compra', '0003_auto_20210218_1834'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proveedor',
            options={'ordering': ['cod_proveedor'], 'verbose_name': 'Proveedor', 'verbose_name_plural': 'Proveedores'},
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='cod_proveedor',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Código Proveedor'),
        ),
    ]
