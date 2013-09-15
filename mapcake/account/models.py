from django.db import models

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


class Groups(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)
    modified = models.TimeField(null=True, blank=True)
    created = models.TimeField()

    class Meta:
        db_table = u'groups'
