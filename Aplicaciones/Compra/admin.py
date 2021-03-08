from django.contrib import admin
from Aplicaciones.Compra.models import*

class proveedorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "cod_proveedor")
    search_fields = ["nombre", "cod_proveedor"]

#class tipoProductoAdmin(admin.ModelAdmin):
 #   list_display=("descripcion","cod_tipo")
  #  search_fields=("descripcion","cod_tipo")

class productosAdmin(admin.ModelAdmin):
    list_display=("nombre_producto","cod_producto")
    search_fields=("nombre_producto","cod_producto")

class CompraAdmin(admin.ModelAdmin):
    list_display=("nro_factura","proveedor")
    search_fields=("nro_factura","proveedor")

class DetalleCompraAdmin(admin.ModelAdmin):
    list_display=("nro_detalle","compra")
    search_fields=("nro_detalle","compra")

#class pedidoCompraAdmin(admin.ModelAdmin):
 #   list_display=("nro_pedido_compra","descripcion_pedido")
  #  search_fields=("nro_pedido_compra","descripcion_pedido")


# Register your models here.

admin.site.register(Proveedor, proveedorAdmin)
#admin.site.register(Tipo_producto,tipoProductoAdmin)
admin.site.register(Producto,productosAdmin)
#admin.site.register(Pedidos_Compra,pedidoCompraAdmin)
admin.site.register(Compra,CompraAdmin)
admin.site.register(CompraDetalle,DetalleCompraAdmin)