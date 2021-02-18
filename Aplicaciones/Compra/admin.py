from django.contrib import admin
from Aplicaciones.Compra.models import*

class proveedorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "cod_proveedor")
    search_fields = ["nombre", "cod_proveedor"]


# Register your models here.

admin.site.register(Proveedor, proveedorAdmin)