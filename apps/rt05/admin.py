# apps/rt05/admin.py

# Django modules
from django.contrib import admin

# Locals
from apps.rt05.models import RT05, Wargart05

# Register your models here.

# admin.site.register(RT05)
@admin.register(RT05)
class RT05Admin(admin.ModelAdmin):
	list_display = ['nama_rt', 'nama_ketua', 'rw']
	list_filter = ['rw']


# admin.site.register(Wargart05)
@admin.register(Wargart05)
class Wargart05Admin(admin.ModelAdmin):
	list_display = [
		'nama_lengkap', 'nik', 'e_ktp', 'hp', 'gender', 'pendidikan', 'yatim', 
		'vaksin', 'covid', 'status_perawatan', 'status_ekonomi']
	list_filter = ['covid','vaksin', 'status_perawatan', 'status_ekonomi', 'e_ktp', 'yatim']