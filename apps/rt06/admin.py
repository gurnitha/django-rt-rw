# apps/rt06/admin.py

# Django modules
from django.contrib import admin

# Locals
from apps.rt06.models import RT06, Wargart06

# Register your models here.

# admin.site.register(RT06)
@admin.register(RT06)
class RT06Admin(admin.ModelAdmin):
	list_display = ['nama_rt', 'nama_ketua', 'rw']
	list_filter = ['rw']


# admin.site.register(Wargart06)
@admin.register(Wargart06)
class Wargart06Admin(admin.ModelAdmin):
	list_display = [
		'nama_lengkap', 'nik', 'e_ktp', 'hp', 'gender', 'pendidikan', 'yatim', 
		'vaksin', 'covid', 'status_perawatan', 'status_ekonomi']
	list_filter = ['covid','vaksin', 'status_perawatan', 'status_ekonomi', 'e_ktp', 'yatim']