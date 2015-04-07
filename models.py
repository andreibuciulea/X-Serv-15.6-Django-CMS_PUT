from django.db import models

# Create your models here.

class Veraneo(models.Model):
    sitio = models.CharField(max_length=32)
    precio = models.PositiveIntegerField()
    duracion = models.PositiveSmallIntegerField()
