from django.contrib import admin
from Aplicaciones.Compra.models import*

class proveedorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "cod_proveedor")
    search_fields = ["nombre", "cod_proveedor"]

#class tipoProductoAdmin(admin.ModelAdmin):
 #   list_display=("descripcion","cod_tipo")
  #  search_fields=("descripcion","cod_tipo")

# Register your models here.

admin.site.register(Proveedor, proveedorAdmin)
#admin.site.register(Tipo_producto,tipoProductoAdmin)
