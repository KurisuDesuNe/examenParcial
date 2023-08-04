from django.db import models

# Create your models here.

class infoProductos(models.Model):
    
    descproducto = models.CharField(max_length=32, blank=True, null=True)
    codigo = models.CharField(max_length=32, blank=True, null=True)
    precioventa = models.CharField(max_length=32, blank=True, null=True)
    cantidad = models.CharField(max_length=32, blank=True, null=True)
    relacionada = models.CharField(max_length=32, blank=True, null=True)

class infoTiendas(models.Model):
    
    direccion = models.CharField(max_length=32, blank=True, null=True)
    provincia = models.CharField(max_length=32, blank=True, null=True)
    region = models.CharField(max_length=32, blank=True, null=True)
    fechacrea = models.CharField(max_length=32, blank=True, null=True)
    telefono = models.CharField(max_length=32, blank=True, null=True)