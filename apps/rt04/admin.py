# apps/rt04/admin.py

# Django modules
from django.contrib import admin

# Locals
from apps.rt04.models import RT04, Wargart04

# Register your models here.

# admin.site.register(RT04)
@admin.register(RT04)
class RT04Admin(admin.ModelAdmin):
	list_display = ['nama_rt', 'nama_ketua', 'rw']
	list_filter = ['rw']


# admin.site.register(Wargart04)
@admin.register(Wargart04)
class Wargart04Admin(admin.ModelAdmin):
	list_display = [
		'nama_lengkap', 'nik', 'e_ktp', 'hp', 'gender', 'pendidikan', 'yatim', 
		'vaksin', 'covid', 'status_perawatan', 'status_ekonomi']
	list_filter = ['covid','vaksin', 'status_perawatan', 'status_ekonomi', 'e_ktp', 'yatim']