# apps/rt03/models.py

# Django modules
from django.db import models

# Locals
from apps.desa.models import Desa
from apps.rw14.models import RW14  
from apps.core.models import AbstractWargaModel
# Create your models here.


class RT03(models.Model):

	nama_rt 	= models.CharField(max_length=50)
	nama_ketua 	= models.CharField(max_length=50)
	alamat_rt 	= models.CharField(max_length=100)
	hp 			= models.CharField(max_length=20, blank=True, null=True)
	telpon 		= models.CharField(max_length=20, blank=True, null=True)
	rw 			= models.ForeignKey(
						RW14, max_length=50, blank=False,
						on_delete=models.CASCADE)
	desa 		= models.ForeignKey(
						Desa, max_length=50, blank=False,
						on_delete=models.CASCADE)	
	
	class Meta:
		verbose_name = "RT 03"
		verbose_name_plural = "RT 03"

	def __str__(self):
		return self.nama_rt


class Wargart03(AbstractWargaModel):
    rt = models.ForeignKey(
                        RT03, 
                        on_delete=models.CASCADE,
                        help_text='Klik tanda panah.')
    def __str__(self):
        return self.nama_lengkap