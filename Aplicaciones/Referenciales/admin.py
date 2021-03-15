from django.contrib import admin
from Aplicaciones.Referenciales.models import *

admin.site.site_header = 'Israel Profi Systens'
admin.site.site_title = 'Bienvenidos'
admin.site.index_title = 'Administracion IsPSys'

class ciudadAdmin(admin.ModelAdmin):
    list_display = ( "cod_ciudad", "nombre")
    search_fields = ("nombre", "cod_ciudad")

class EmpleadoAdmin(admin.ModelAdmin):
   list_display = ( "cod_empleado", "nombre")
   search_fields = ( "cod_empleado","nombre")

class CondicionAdmin(admin.ModelAdmin):
  list_display = ( "cod_condicion", "descripcion_cond")
  search_fields = ( "cod_condicion","descripcion_cond")


# Register your models here.

admin.site.register(Ciudad, ciudadAdmin)
admin.site.register(Empleado,EmpleadoAdmin)
admin.site.register(Condicion,CondicionAdmin)

