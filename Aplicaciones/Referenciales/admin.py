from django.contrib import admin
from Aplicaciones.Referenciales.models import *

admin.site.site_header = 'Israel Profi Systens'
admin.site.site_title = 'Bienvenidos'
admin.site.index_title = 'Administracion IsPSys'

class ciudadAdmin(admin.ModelAdmin):
    list_display = ("nombre", "cod_ciudad")
    search_fields = ("nombre", "cod_ciudad")

# Register your models here.

admin.site.register(Ciudad, ciudadAdmin)