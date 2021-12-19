# apps/rw/models.py

# Django modules
from django.db import models

# Locals
from apps.desa.models import Desa

# Create your models here.

class RW14(models.Model):

	nama_rw 		= models.CharField(max_length=50)
	nama_ketua_rw 	= models.CharField(max_length=50)
	alamat_rw 		= models.CharField(max_length=100)
	hp 				= models.CharField(max_length=20, blank=True, null=True)
	telpon 			= models.CharField(max_length=20, blank=True, null=True)
	desa 			= models.ForeignKey(
							Desa, max_length=50, blank=False,
							on_delete=models.CASCADE)	

	class Meta:
		verbose_name = "RW 14"
		verbose_name_plural = "RW 14"

	def __str__(self):
		return self.nama_rw