# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Rhythm'
        db.create_table('dances_rhythm', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100, unique=True, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('dances', ['Rhythm'])

        # Adding model 'Level'
        db.create_table('dances_level', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('dances', ['Level'])

        # Adding model 'DanceStep'
        db.create_table('dances_dancestep', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True, null=True, blank=True)),
            ('rhythm', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'dancesteps', null=True, to=orm['dances.Rhythm'])),
            ('level', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'level', null=True, to=orm['dances.Level'])),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('dica', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('features', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('dances', ['DanceStep'])


    def backwards(self, orm):
        # Deleting model 'Rhythm'
        db.delete_table('dances_rhythm')

        # Deleting model 'Level'
        db.delete_table('dances_level')

        # Deleting model 'DanceStep'
        db.delete_table('dances_dancestep')


    models = {
        'dances.dancestep': {
            'Meta': {'ordering': "['name']", 'object_name': 'DanceStep'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'dica': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'features': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'level'", 'null': 'True', 'to': "orm['dances.Level']"}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'rhythm': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dancesteps'", 'null': 'True', 'to': "orm['dances.Rhythm']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        'dances.level': {
            'Meta': {'ordering': "['name']", 'object_name': 'Level'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'dances.rhythm': {
            'Meta': {'ordering': "['name']", 'object_name': 'Rhythm'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'update_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['dances']