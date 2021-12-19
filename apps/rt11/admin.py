# apps/rt11/admin.py

# Django modules
from django.contrib import admin

# Locals
from apps.rt11.models import RT11, Wargart11

# Register your models here.

# admin.site.register(RT11)
@admin.register(RT11)
class RT11Admin(admin.ModelAdmin):
	list_display = ['nama_rt', 'nama_ketua', 'rw']
	list_filter = ['rw']


# admin.site.register(Wargart11)
@admin.register(Wargart11)
class Wargart11Admin(admin.ModelAdmin):
	list_display = [
		'nama_lengkap', 'nik', 'e_ktp', 'hp', 'gender', 'pendidikan', 'yatim', 
		'vaksin', 'covid', 'status_perawatan', 'status_ekonomi']
	list_filter = ['covid','vaksin', 'status_perawatan', 'status_ekonomi', 'e_ktp', 'yatim']