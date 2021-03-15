from django.db import models

# Create your models here.

class Ciudad(models.Model):
    cod_ciudad = models.AutoField(primary_key=True, verbose_name="Código Ciudad")
    nombre = models.CharField(max_length=50,unique=True, verbose_name="Ciudad")

    def __str__(self):
        return "{0}".format(self.nombre)

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
        db_table = 'ciudad'
        ordering = ['cod_ciudad']

class Empleado(models.Model):
    cod_empleado = models.AutoField(primary_key=True, verbose_name="Codigo Empleado")
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    apellido = models.CharField(max_length=50, verbose_name="Apellido")
    cedula=models.IntegerField(unique=True)
    direccion=models.CharField(max_length=100)
    ciudad = models.ForeignKey(Ciudad, blank=False, null=False, on_delete=models.PROTECT)
    telefono=models.IntegerField()
    email = models.EmailField(max_length=50, blank=True, null=True)
    fecha_inic_contrato= models.DateField(auto_now=True)
    
    def __str__(self):
        return "{0} {1}".format(self.nombre, self.cod_empleado)
        
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'
        ordering = ['cod_empleado']


class Condicion(models.Model):
    cod_condicion = models.AutoField(primary_key=True, verbose_name="Codigo Condicion")
    descripcion= (
        ('0', 'Contado'),
        ('1', 'Credito'),
    )
    descripcion_cond= models.CharField(max_length=2, choices=descripcion,default='0')
    plazo = models.IntegerField()

    def __str__(self):
        return "{0} ".format(self.cod_condicion)

    class Meta:
        verbose_name = 'Condicion'
        verbose_name_plural = 'Condiciones'
        db_table = 'condicion'
        ordering = ['cod_condicion']
    
class TipoDocumento(models.Model):
    cod_tipo_doc = models.AutoField(primary_key=True, verbose_name="Codigo Tipo Documento")
    descripcion= models.CharField(max_length=30)
    nro_timbrado = models.IntegerField()
    fecha_inicio=models.DateField(auto_now=True)
    fecha_fin=models.DateField()
    estado=models.CharField(max_length=1)

    def __str__(self):
        return "{0} ".format(self.cod_tipo_doc)

    class Meta:
        verbose_name = 'TipoDocumento'
        verbose_name_plural = 'TipoDocumentos'
        db_table = 'tipo_documento'
        ordering = ['cod_tipo_doc']
