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


class Producto(models.Model):
    cod_producto = models.IntegerField(primary_key=True,verbose_name = "Codigo Producto")
    TIPO_PRODUCTO= (
        ('1', 'Producto'),
        ('2', 'Servicio'),
    )
    tipo_producto= models.CharField(max_length=2, choices=TIPO_PRODUCTO,default='1')
    nombre_producto = models.CharField(max_length=50,verbose_name="producto",unique=True)
    descripcion = models.CharField(max_length=30,blank=True)
    marca=models.CharField(max_length=30)
    #cod_tipo = models.ForeignKey(Tipo_producto,blank=False,null=False,on_delete=models.PROTECT)
    cant_stock = models.IntegerField()
    cant_minima_stock = models.IntegerField(default=1)
    estado=models.CharField(max_length=15)

    def __str__(self):
        return "{0} {1}".format(self.cod_producto,self.nombre_producto)

    class Meta:
        verbose_name ='Producto'
        verbose_name_plural ='Productos'
        db_table = 'producto'

class DetalllePrecioCompra(models.Model):
    ultima_fecha_precio = models.DateField(primary_key=True, verbose_name = "Fecha Detalle Precio")
    producto = models.ForeignKey(Producto,blank=False,null=False,on_delete=models.PROTECT)
    precio_compra=models.FloatField()
    def __str__(self):
        return "{0}".format(self.ultima_fecha_precio)

    class Meta:
        verbose_name = 'DetallePrecioCompra'
        verbose_name_plural = 'DetallePrecioCompras'
        db_table = 'detalle_precio_compra'
        ordering = ['ultima_fecha_precio']

class Compra(models.Model):
    nro_factura=models.CharField(max_length=15,primary_key=True, verbose_name = "Numero Factura")
    tipo_compra=models.CharField(max_length=10)
    tipo_documento=models.ForeignKey(TipoDocumento,blank=False,null=False,on_delete=models.PROTECT)
    proveedor=models.ForeignKey(Proveedor,blank=False,null=False,on_delete=models.PROTECT)
    fecha_emision=models.DateField(auto_now=True)
    empleado=models.ForeignKey(Empleado,blank=False,null=False,on_delete=models.PROTECT)
    cod_condicion=(
        ('0', 'Contado'),
        ('1', 'Credito'),
    )
    condicion = models.CharField(max_length=2, choices=cod_condicion,default='0')
    total_IVA=models.FloatField()
    total_descuento=models.FloatField()
    total_importe=models.FloatField()

    def __str__(self):
        return "{0}".format(self.nro_factura)

    class Meta:
        verbose_name ='Compra'
        verbose_name_plural ='Compras'
        db_table = 'compra'
        ordering = ['nro_factura']

class CompraDetalle(models.Model):
    nro_detalle=models.CharField(max_length=15,primary_key=True, verbose_name = "Numero Detalle compra")
    compra=models.ForeignKey(Compra,blank=False,null=False,on_delete=models.PROTECT)
    producto=models.ForeignKey(Producto,blank=False,null=False,on_delete=models.PROTECT)
    cantidad=models.IntegerField()
    total_IVA=models.FloatField()
    total_descuento=models.FloatField()
    total_importe=models.FloatField()
    
    def __str__(self):
        return "{0}".format(self.nro_detalle)

    class Meta:
        verbose_name ='Detalle_compra'
        verbose_name_plural ='Detalle_compras'
        db_table = 'detalle_compra'

        


class Movimiento(models.Model):
    cod_movimiento = models.AutoField(primary_key=True, verbose_name="Codigo Movimiento")
    tipo_movimiento =models.CharField(max_length=30)

    def __str__(self):
        return "{0} ".format(self.cod_movimiento)

    class Meta:
        verbose_name = 'Movimiento'
        verbose_name_plural = 'Movimientos'
        db_table = 'movimiento'
        ordering = ['cod_movimiento']

class MovimientoProducto(models.Model):
    fecha_movimiento_producto = models.DateField(primary_key=True, verbose_name="Fecha Movimiento Producto ")
    movimiento_producto =models.ForeignKey(Movimiento, blank=False, null=False, on_delete=models.PROTECT)
    detalle_compra=models.ForeignKey(CompraDetalle, blank=False, null=False, on_delete=models.PROTECT)
    cantidad_producto=models.ImageField()

    def __str__(self):
        return "{0} ".format(self.fecha_movimiento_producto)

    class Meta:
        verbose_name = 'MovimientoProducto'
        verbose_name_plural = 'MovimientoProductos'
        db_table = 'movimiento_producto'
        ordering = ['fecha_movimiento_producto']