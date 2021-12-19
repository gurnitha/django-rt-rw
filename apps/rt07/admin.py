# apps/rt07/admin.py

# Django modules
from django.contrib import admin

# Locals
from apps.rt07.models import RT07, Wargart07

# Register your models here.

# admin.site.register(RT07)
@admin.register(RT07)
class RT07Admin(admin.ModelAdmin):
	list_display = ['nama_rt', 'nama_ketua', 'rw']
	list_filter = ['rw']


# admin.site.register(Wargart07)
@admin.register(Wargart07)
class Wargart07Admin(admin.ModelAdmin):
	list_display = [
		'nama_lengkap', 'nik', 'hp', 'gender', 'pendidikan', 'yatim', 
		'vaksin', 'covid', 'status_perawatan', 'status_ekonomi']
	list_filter = ['covid','vaksin', 'status_perawatan', 'status_ekonomi', 'yatim']