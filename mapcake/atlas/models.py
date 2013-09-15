from django.db import models
from account.models import Users


class Atlases(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128, unique=True)
    abstract = models.TextField(blank=True)
    createdby = models.ForeignKey(Users, db_column='createdby')
    created = models.DateTimeField(null=True, blank=True)
    modified = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = u'atlases'
