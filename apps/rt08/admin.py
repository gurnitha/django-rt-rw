# apps/rt08/admin.py

# Django modules
from django.contrib import admin

# Locals
from apps.rt08.models import RT08, Wargart08

# Register your models here.

# admin.site.register(RT08)
@admin.register(RT08)
class RT08Admin(admin.ModelAdmin):
	list_display = ['nama_rt', 'nama_ketua', 'rw']
	list_filter = ['rw']


# admin.site.register(Wargart08)
@admin.register(Wargart08)
class Wargart08Admin(admin.ModelAdmin):
	list_display = [
		'nama_lengkap', 'nik', 'e_ktp', 'hp', 'gender', 'pendidikan', 'yatim', 
		'vaksin', 'covid', 'status_perawatan', 'status_ekonomi']
	list_filter = ['covid','vaksin', 'status_perawatan', 'status_ekonomi', 'e_ktp', 'yatim']