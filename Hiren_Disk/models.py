from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class DiskBox(models.Model):
	user = models.ForeignKey(User)
	diskBoxNo = models.IntegerField(max_length=128, verbose_name = "Disk Box Number")
	class Meta:
		verbose_name = "Disk Box"
	def __unicode__(self):
		return u'%i' % self.diskBoxNo

class DiskList(models.Model):
	diskbox = models.ForeignKey(DiskBox)
	diskName = models.CharField(max_length=500, verbose_name=u'Disk Name')
	class Meta:
		verbose_name = "Disk List"
	def __unicode__(self):
		return self.diskName