from django.db import models

# Create your models here.
class Empleado(models.Model):
    cod_empleado = models.CharField(primary_key=True, max_length=8, verbose_name='Código')
    nombres = models.CharField(max_length=20, verbose_name='Nombres')
    apellidos = models.CharField(max_length=20, verbose_name='Apellidos')

def __str__(self):
    return "{0} {1}".format(self.nombres, self.apellidos)
