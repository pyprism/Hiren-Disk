from django.contrib import admin
from disk.models import Box, Disk
# Register your models here.

admin.site.register([Box, Disk])