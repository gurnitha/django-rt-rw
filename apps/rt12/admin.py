# apps/rt12/admin.py

# Django modules
from django.contrib import admin

# Locals
from apps.rt12.models import RT12, Wargart12

# Register your models here.

# admin.site.register(RT12)
@admin.register(RT12)
class RT12Admin(admin.ModelAdmin):
	list_display = ['nama_rt', 'nama_ketua', 'rw']
	list_filter = ['rw']


# admin.site.register(Wargart12)
@admin.register(Wargart12)
class Wargart12Admin(admin.ModelAdmin):
	list_display = [
		'nama_lengkap', 'nik', 'e_ktp', 'hp', 'gender', 'pendidikan', 'yatim', 
		'vaksin', 'covid', 'status_perawatan', 'status_ekonomi']
	list_filter = ['covid','vaksin', 'status_perawatan', 'status_ekonomi', 'e_ktp', 'yatim']
