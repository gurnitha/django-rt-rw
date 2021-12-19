# apps/rt09/admin.py

# Django modules
from django.contrib import admin

# Locals
from apps.rt09.models import RT09, Wargart09

# Register your models here.

# admin.site.register(RT09)
@admin.register(RT09)
class RT09Admin(admin.ModelAdmin):
	list_display = ['nama_rt', 'nama_ketua', 'rw']
	list_filter = ['rw']


# admin.site.register(Wargart09)
@admin.register(Wargart09)
class Wargart09Admin(admin.ModelAdmin):
	list_display = [
		'nama_lengkap', 'nik', 'e_ktp', 'hp', 'gender', 'pendidikan', 'yatim', 
		'vaksin', 'covid', 'status_perawatan', 'status_ekonomi']
	list_filter = ['covid','vaksin', 'status_perawatan', 'status_ekonomi', 'e_ktp', 'yatim']
	search_fields = ['nama_lengkap', 'vaksin', 'covid']