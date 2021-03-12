from django.db import models
from Aplicaciones.Referenciales.models import*

# Create your models here.

class Proveedor(models.Model):
    cod_proveedor = models.AutoField(primary_key=True, verbose_name = "Código Proveedor")
    nombre = models.CharField(max_length=20, unique=True,verbose_name= "Proveedor")
    ruc = models.CharField(max_length=15,unique=True)
    telefono = models.CharField(max_length=12)
    direccion = models.CharField(max_length=100)
    timbrado = models.IntegerField()
    email = models.EmailField(max_length=20, blank=True, null=True)
    ciudad = models.ForeignKey(Ciudad, blank=False, null=False, on_delete=models.PROTECT)

    def __str__(self):
        return "{0} {1}".format(self.nombre, self.cod_proveedor)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        db_table = 'proveedor'
        ordering = ['cod_proveedor']
    

#class Tipo_producto(models.Model):
 #   cod_tipo=models.IntegerField(primary_key=True,verbose_name="Codigo Tipo Producto")
  #  descripcion=models.CharField(max_length=30,verbose_name="Tipo Producto")

   # def __str__(self):
    #    return "{0} {1}".format(self.cod_tipo,self.descripcion)

    #class Meta:
     #   verbose_name= 'Tipo Producto'
      #  db_table='tipo_producto'
