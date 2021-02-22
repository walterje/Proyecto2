from django.db import models

# Create your models here.

class Ciudad(models.Model):
    cod_ciudad = models.AutoField(primary_key=True, verbose_name="Código Ciudad")
    nombre = models.CharField(max_length=30, verbose_name="Ciudad")

    def __str__(self):
        return "{0} {1}".format(self.nombre, self.cod_ciudad)

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
        db_table = 'ciudad'
        ordering = ['cod_ciudad']