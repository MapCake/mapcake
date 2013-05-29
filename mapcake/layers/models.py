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


class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=128, blank=True)
    surname = models.CharField(max_length=256, blank=True)
    email = models.CharField(max_length=256)
    password = models.CharField(max_length=512)
    group_id = models.IntegerField()
    created = models.TimeField()
    modified = models.TimeField(null=True, blank=True)

    class Meta:
        db_table = u'users'


class Types(models.Model):
    id = models.IntegerField(primary_key=True)
    # Field name made lowercase. This field type is a guess.
    type = models.TextField(db_column='Type', blank=True)

    class Meta:
        db_table = u'types'


class Sources(models.Model):
    id = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=128, unique=True)
    source = models.TextField(blank=True)  # This field type is a guess.
    # Field name made lowercase. This field type is a guess.
    ddbuser = models.CharField(db_column='DDBuser', blank=True, max_length=128)
    password = models.CharField(blank=True, max_length=128)
    type = models.TextField(
        Types, null=True, db_column='type', blank=True)
    # champ destine a contenir les urls des services
    url = models.TextField(blank=True, db_column='url')

    class Meta:
        db_table = u'sources'


class Layers(models.Model):
    id = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=128, unique=True)
    abstract = models.TextField(blank=True)
    createdby = models.ForeignKey(
        Users, null=True, db_column='createdby', blank=True, editable=False)
    creation_date = models.DateTimeField(
        null=True, blank=True, editable=False, auto_now_add=True)
    modification_date = models.DateTimeField(
        null=True, blank=True, editable=False, auto_now=True)
    source = models.ForeignKey(
        Sources, null=True, blank=True, editable=False,
        db_column='source')

    class Meta:
        db_table = u'layers'


class Groups(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)
    modified = models.TimeField(null=True, blank=True)
    created = models.TimeField()

    class Meta:
        db_table = u'groups'


class Maps(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128, unique=True)
    abstract = models.TextField(blank=True)
    createdby = models.ForeignKey(Users, db_column='createdby')
    created = models.DateTimeField(null=True, blank=True)
    modified = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = u'maps'


class Atlases(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128, unique=True)
    abstract = models.TextField(blank=True)
    createdby = models.ForeignKey(Users, db_column='createdby')
    created = models.DateTimeField(null=True, blank=True)
    modified = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = u'atlases'

# les tables de liaison


class AtlasesMaps(models.Model):
    id = models.ForeignKey(Maps, primary_key=True, db_column='id')
    atlas = models.ForeignKey(Atlases)
    map_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = u'atlases_maps'


class LayersMaps(models.Model):
    id = models.IntegerField(primary_key=True)
    map_id = models.ForeignKey(Maps, db_column='id')
    layer_id = models.ForeignKey(Layers, db_column='id')

    class Meta:
        db_table = u'layers_maps'