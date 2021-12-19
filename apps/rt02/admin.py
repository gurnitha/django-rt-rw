# apps/rt02/admin.py

# Django modules
from django.contrib import admin

# Locals
from apps.rt02.models import RT02, Wargart02

# Register your models here.

# admin.site.register(RT02)
@admin.register(RT02)
class RT02Admin(admin.ModelAdmin):
	list_display = ['nama_rt', 'nama_ketua', 'rw']
	list_filter = ['rw']


# admin.site.register(Wargart02)
@admin.register(Wargart02)
class Wargart02Admin(admin.ModelAdmin):
	list_display = [
		'nama_lengkap', 'nik', 'e_ktp', 'hp', 'gender', 'pendidikan', 'yatim', 
		'vaksin', 'covid', 'status_perawatan', 'status_ekonomi']
	list_filter = ['covid','vaksin', 'status_perawatan', 'status_ekonomi', 'e_ktp', 'yatim']