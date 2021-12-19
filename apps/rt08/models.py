# apps/rt08/models.py

# Django modules
from django.db import models

# Locals
from apps.desa.models import Desa
from apps.rw14.models import RW14  
from apps.core.models import AbstractWargaModel
# Create your models here.


class RT08(models.Model):

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
		verbose_name = "RT 08"
		verbose_name_plural = "RT 08"

	def __str__(self):
		return self.nama_rt


class Wargart08(AbstractWargaModel):
    rt = models.ForeignKey(
                        RT08, 
                        on_delete=models.CASCADE,
                        help_text='Klik tanda panah.')
    def __str__(self):
        return self.nama_lengkap