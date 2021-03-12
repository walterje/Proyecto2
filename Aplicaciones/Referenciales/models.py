from django.db import models

# Create your models here.

class Ciudad(models.Model):
    cod_ciudad = models.AutoField(primary_key=True, verbose_name="Código Ciudad")
    nombre = models.CharField(max_length=30,unique=True, verbose_name="Ciudad")

    def __str__(self):
        return "{0}".format(self.nombre)

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
        db_table = 'ciudad'
        ordering = ['cod_ciudad']

class Empleado(models.Model):
    cod_empleado = models.AutoField(primary_key=True, verbose_name="Código Empleado")
    nombre = models.CharField(max_length=20, verbose_name="Nombre")
    apellido = models.CharField(max_length=20, verbose_name="Apellido")
    cedula=models.IntegerField(unique=True)
    direccion=models.CharField(max_length=100)
    ciudad = models.ForeignKey(Ciudad, blank=False, null=False, on_delete=models.PROTECT)
    telefono=models.IntegerField()
    email = models.EmailField(max_length=20, blank=True, null=True)
    fecha_inic_contrato= models.DateField(auto_now=True)



    def __str__(self):
        return "{0} {1}".format(self.nombre, self.cod_empleado)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'
        ordering = ['cod_empleado']
    

