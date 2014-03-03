# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models,
#but don't rename db_table values or field names.

# Also note: You'll have to insert the output of
#'django-admin.py sqlcustom [appname]'
# into your database.

from django.contrib.gis.db import models
from django.contrib.auth.models import User

class Types(models.Model):
    id = models.IntegerField(primary_key=True)
    # Field name made lowercase. This field type is a guess.
    type = models.TextField(db_column='Type', blank=True)

    class Meta:
        db_table = u'types'


class Layers(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128, unique=True)
    source = models.TextField(blank=True)  # This field type is a guess.
    abstract = models.TextField(blank=True)
    ddbuser = models.CharField(db_column='DDBuser', blank=True, max_length=128)
    password = models.CharField(blank=True, max_length=128)
    type = models.TextField(
        Types, null=True, db_column='type', blank=True)
    # field for the url of the service
    url = models.TextField(blank=True, db_column='url')

    createdby = models.ForeignKey(
        User, null=True, db_column='createdby', blank=True, editable=False)
    creation_date = models.DateTimeField(
        null=True, blank=True, editable=False, auto_now_add=True)
    modification_date = models.DateTimeField(
        null=True, blank=True, editable=False, auto_now=True)
    isPrivate = models.BooleanField(null=False,blank=False, default=True)


