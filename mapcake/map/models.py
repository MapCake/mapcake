from django.db import models
from django.contrib.auth.models import User
from atlas.models import Atlases

class Maps(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128, unique=True)
    abstract = models.TextField(blank=True)
    createdby = models.ForeignKey(User, db_column='createdby')
    created = models.DateTimeField(null=True, blank=True)
    modified = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = u'maps'


# faire la correction
class AtlasesMaps(models.Model):
    id = models.ForeignKey(Maps, primary_key=True, db_column='id')
    atlas = models.ForeignKey(Atlases)
    map_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = u'atlases_maps'

