from django.contrib import admin
from Hiren_Disk.models import DiskBox, DiskList
# Register your models here.

class DiskBoxAdmin(admin.ModelAdmin):
	list_display = ('diskBoxNo','diskName')
	search_fields = ('diskName')

admin.site.register([DiskBox,DiskList],DiskBoxAdmin,)