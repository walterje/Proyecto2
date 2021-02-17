from django.db import models

# Create your models here.

class Ciudad(models.Model):
    cod_ciudad = models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)