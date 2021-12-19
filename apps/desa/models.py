# apps/desa/models.py

# Django modules
from django.db import models

# Create your models here.

class Desa(models.Model):

	nama_desa 	= models.CharField(max_length=50)
	nama_kades 	= models.CharField(max_length=50)
	alamat_desa = models.CharField(max_length=100)
	hp 			= models.CharField(max_length=20, blank=True, null=True)
	telpon 		= models.CharField(max_length=20, blank=True, null=True)

	class Meta:
		verbose_name = "Desa"
		verbose_name_plural = "Desa"

	def __str__(self):
		return self.nama_desa
