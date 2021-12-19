# apps/rt01/admin.py

# Django modules
from django.contrib import admin

# Locals
from apps.rt01.models import RT01, Wargart01

# Register your models here.

# admin.site.register(RT01)
@admin.register(RT01)
class RT01Admin(admin.ModelAdmin):
	list_display = ['nama_rt', 'nama_ketua', 'rw']
	list_filter = ['rw']


# admin.site.register(Wargart01)
@admin.register(Wargart01)
class Wargart01Admin(admin.ModelAdmin):
	list_display = [
		'nama_lengkap', 'nik', 'e_ktp', 'hp', 'gender', 'pendidikan', 'yatim', 
		'vaksin', 'covid', 'status_perawatan', 'status_ekonomi']
	list_filter = ['covid','vaksin', 'status_perawatan', 'status_ekonomi', 'e_ktp', 'yatim']