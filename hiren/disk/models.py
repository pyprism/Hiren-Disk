from django.db import models

# Create your models here.


class Box(models.Model):
    disk_no = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        #return str(self.disk_no)
        return "%s %s" % (self.disk_no, self.created_at)


class Disk(models.Model):
    box_no = models.ForeignKey(Box)
    serial = models.IntegerField()
    titles = models.TextField()

    def __str__(self):
        return '%s %s' % (self.serial, self.titles)