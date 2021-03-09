# Generated by Django 3.1.5 on 2021-03-07 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Referenciales', '0003_auto_20210218_2326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('cod_empleado', models.AutoField(primary_key=True, serialize=False, verbose_name='Código Empleado')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=20, verbose_name='Apellido')),
                ('cedula', models.IntegerField()),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(blank=True, max_length=20, null=True)),
                ('fecha_inic_contrato', models.DateField(auto_now=True)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Referenciales.ciudad')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'db_table': 'empleado',
                'ordering': ['cod_empleado'],
            },
        ),
    ]