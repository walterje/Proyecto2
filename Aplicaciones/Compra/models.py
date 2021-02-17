from django.db import models
from Aplicaciones.Referenciales.models import*

# Create your models here.

class Proveedor(models.Model):
    cod_proveedor = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    ruc = models.CharField(max_length=15)
    telefono = models.CharField(max_length=12)
    direccion = models.CharField(max_length=100)
    timbrado = models.IntegerField()
    email = models.EmailField(max_length=20, blank=True, null=True)
    ciudad = models.ForeignKey(Ciudad, blank=False, null=False, on_delete=models.PROTECT)

def __str__(self):
    return "{0} {1}".format(self.nombre, self.apellido)
    
