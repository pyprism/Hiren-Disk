from django.db import models


class Box(models.Model):
    box_no = models.IntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" % (self.box_no, self.created_at)


class Disk(models.Model):
    disk_no = models.ForeignKey(Box)
    serial = models.IntegerField(unique=True)
    contents = models.TextField()

    def __str__(self):
        return '%s %s' % (self.serial, self.contents)