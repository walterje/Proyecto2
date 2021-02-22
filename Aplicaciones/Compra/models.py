from django.db import models
from Aplicaciones.Referenciales.models import*

# Create your models here.

class Proveedor(models.Model):
    cod_proveedor = models.AutoField(primary_key=True, verbose_name = "Código Proveedor")
    nombre = models.CharField(max_length=20, verbose_name= "Proveedor")
    ruc = models.CharField(max_length=15)
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
    

class Tipo_producto(models.Model):
    cod_tipo_producto=models.IntegerField(primary_key=True,verbose_name="Codigo Tipo Producto")
    descripcion=models.CharField(max_length=30,verbose_name="Tipo Producto")

    def __str__(self):
        return "{0} {1}".format(self.cod_tipo,self.descripcion)

    class Meta:
        verbose_name= 'Tipo Producto'
        db_table='Tipo_producto'

class Producto(models.Model):
    cod_producto = models.IntegerField(primary_key=True,verbose_name = "Codigo Producto")
    nombre_producto = models.CharField(max_length=30,verbose_name="producto")
    descripcion = models.CharField(max_length=30)
    cod_tipo_producto = models.ForeignKey(Tipo_producto,blank=False,null=False,on_delete=models.PROTECT)
    cant_stock = models.IntegerField()
    cant_minima_stock = models.IntegerField()
    estado=models.CharField(max_length=15)

    def __str__(self):
        return "{0} {1}".format(self.cod_producto,self.descripcion)

    class Meta:
        verbose_name ='Producto'
        verbose_name_plural ='Productos'
        db_table = 'Producto'

class Pedidos_Compra(models.Model):
   nro_pedido_compra = models.IntegerField(primary_key=True,verbose_name="Numero Pedido")
   fecha_pedido_compra=models.DateField(auto_now=True)
   cod_proveedor=models.ForeignKey(Proveedor,blank= False, null=False, on_delete=models.PROTECT) 
   cod_producto=models.ForeignKey(Producto,blank= False, null=False, on_delete=models.PROTECT)
   cantidad=models.IntegerField()
   descripcion_pedido=models.CharField(max_length=50,verbose_name="Pedido_compra")
   
   def __str__(self):
        return "{0} {1}".format(self.nro_pedido_compra,self.descripcion_pedidio)
    
   class Meta:
       verbose_name = 'Pedido_compra'
       verbose_name_plural = 'Pedidos_compras'
       db_table = 'Pedido_compra'


