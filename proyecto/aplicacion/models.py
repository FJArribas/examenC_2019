#from __future__ import unicode_literals 

import django
from django.db import models

from django.template.defaultfilters import slugify

# Create your models here.

class camion(models.Model):

	nombreC = models.CharField(max_length=128)

	def save(self, *args, **kwargs):
		super(camion, self).save(*args, **kwargs)

class objeto(models.Model):

	nombreO = models.CharField(max_length=128)

	def save(self, *args, **kwargs):
		super(objeto, self).save(*args, **kwargs)


class ruta(models.Model):
    fechaDeReparto = models.DateTimeField(null=False, auto_now=True)
	medico = models.ForeignKey(camion,on_delete=models.CASCADE)
	objeto = models.ForeignKey(objeto,on_delete=models.CASCADE)

	def save(self, *args, **kwargs):
		super(Receta, self).save(*args, **kwargs)
