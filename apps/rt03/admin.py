# apps/rt03/admin.py

# Django modules
from django.contrib import admin

# Locals
from apps.rt03.models import RT03, Wargart03

# Register your models here.

# admin.site.register(RT03)
@admin.register(RT03)
class RT03Admin(admin.ModelAdmin):
	list_display = ['nama_rt', 'nama_ketua', 'rw']
	list_filter = ['rw']


# admin.site.register(Wargart03)
@admin.register(Wargart03)
class Wargart03Admin(admin.ModelAdmin):
	list_display = [
		'nama_lengkap', 'nik', 'e_ktp', 'hp', 'gender', 'pendidikan', 'yatim', 
		'vaksin', 'covid', 'status_perawatan', 'status_ekonomi']
	list_filter = ['covid','vaksin', 'status_perawatan', 'status_ekonomi', 'e_ktp', 'yatim']