# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Types'
        db.create_table(u'types', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.TextField')(db_column='Type', blank=True)),
        ))
        db.send_create_signal(u'layers', ['Types'])

        # Adding model 'Layers'
        db.create_table(u'sources', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('source', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('abstract', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('ddbuser', self.gf('django.db.models.fields.CharField')(max_length=128, db_column='DDBuser', blank=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('type', self.gf('django.db.models.fields.TextField')(null=True, db_column='type', blank=True)),
            ('url', self.gf('django.db.models.fields.TextField')(db_column='url', blank=True)),
            ('createdby', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, db_column='createdby', blank=True)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('modification_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'layers', ['Layers'])

        # Adding model 'GrpLayers'
        db.create_table(u'layers', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['layers.Layers'], null=True, db_column='source', blank=True)),
        ))
        db.send_create_signal(u'layers', ['GrpLayers'])


    def backwards(self, orm):
        # Deleting model 'Types'
        db.delete_table(u'types')

        # Deleting model 'Layers'
        db.delete_table(u'sources')

        # Deleting model 'GrpLayers'
        db.delete_table(u'layers')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'layers.grplayers': {
            'Meta': {'object_name': 'GrpLayers', 'db_table': "u'layers'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['layers.Layers']", 'null': 'True', 'db_column': "'source'", 'blank': 'True'}),
            'titre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'layers.layers': {
            'Meta': {'object_name': 'Layers', 'db_table': "u'sources'"},
            'abstract': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'createdby': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'db_column': "'createdby'", 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'ddbuser': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_column': "'DDBuser'", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modification_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'source': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'titre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'type': ('django.db.models.fields.TextField', [], {'null': 'True', 'db_column': "'type'", 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'db_column': "'url'", 'blank': 'True'})
        },
        u'layers.types': {
            'Meta': {'object_name': 'Types', 'db_table': "u'types'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.TextField', [], {'db_column': "'Type'", 'blank': 'True'})
        }
    }

    complete_apps = ['layers']