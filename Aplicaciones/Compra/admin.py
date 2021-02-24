from django.contrib import admin
from Aplicaciones.Compra.models import*

class proveedorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "cod_proveedor")
    search_fields = ["nombre", "cod_proveedor"]

class tipoProductoAdmin(admin.ModelAdmin):
    list_display=("cod_tipo","descripcion")
    search_fields=("cod_tipo","descripcion")

class productosAdmin(admin.ModelAdmin):
    list_display=("cod_producto","nombre_producto")
    search_fields=("cod_producto","nombre_producto")

class pedidoCompraAdmin(admin.ModelAdmin):
    list_display=("nro_pedido_compra","descripcion_pedido")
    search_fields=("nro_pedido_compra","descripcion_pedido")
# Register your models here.

admin.site.register(Proveedor, proveedorAdmin)
admin.site.register(Tipo_producto,tipoProductoAdmin)
admin.site.register(Producto,productosAdmin)
admin.site.register(Pedidos_Compra,pedidoCompraAdmin)