from __future__ import unicode_literals

from django.db import models

class Alerta(models.Model):
	codProduct = models.Foreignkey(ProductAssignment, on_delete=models.CASCADE, verbose_name='codigo del producto asignado')
	