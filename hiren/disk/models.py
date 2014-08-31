from django.db import models
from djorm_pgfulltext.models import SearchManager
from djorm_pgfulltext.fields import VectorField


class Box(models.Model):
    box_no = models.IntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" % (self.box_no, self.created_at)


class Disk(models.Model):
    disk_no = models.ForeignKey(Box)
    serial = models.IntegerField(unique=True)
    contents = models.TextField()

    search_index = VectorField()

    objects = SearchManager(
        fields=contents,
        config='pg_catalog.english',
        search_field='search_index',
        auto_update_search_field=True
    )

    def __str__(self):
        return '%s %s' % (self.serial, self.contents)