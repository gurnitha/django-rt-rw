# apps/rt10/admin.py

# Django modules
from django.contrib import admin

# Locals
from apps.rt10.models import RT10, Wargart10

# Register your models here.

# admin.site.register(RT10)
@admin.register(RT10)
class RT10Admin(admin.ModelAdmin):
	list_display = ['nama_rt', 'nama_ketua', 'rw']
	list_filter = ['rw']


# admin.site.register(Wargart10)
@admin.register(Wargart10)
class Wargart10Admin(admin.ModelAdmin):
	list_display = [
		'nama_lengkap', 'nik', 'e_ktp', 'hp', 'gender', 'pendidikan', 'yatim', 
		'vaksin', 'covid', 'status_perawatan', 'status_ekonomi']
	list_filter = ['covid','vaksin', 'status_perawatan', 'status_ekonomi', 'e_ktp', 'yatim']