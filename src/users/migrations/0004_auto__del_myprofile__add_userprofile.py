# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'MyProfile'
        db.delete_table('users_myprofile')

        # Adding model 'UserProfile'
        db.create_table('users_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mugshot', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('privacy', self.gf('django.db.models.fields.CharField')(default='registered', max_length=15)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(related_name='my_profile', unique=True, to=orm['auth.User'])),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('gender', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('monthly_payment', self.gf('django.db.models.fields.DecimalField')(default=50, max_digits=10, decimal_places=1)),
            ('age', self.gf('django.db.models.fields.CharField')(max_length=3, blank=True)),
            ('mobile', self.gf('django.db.models.fields.CharField')(max_length=11)),
            ('tele2', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('facebook', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('interests', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('myteam', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['users.Team'])),
        ))
        db.send_create_signal('users', ['UserProfile'])

        # Removing M2M table for field members on 'Team'
        db.delete_table('users_team_members')


    def backwards(self, orm):
        
        # Adding model 'MyProfile'
        db.create_table('users_myprofile', (
            ('interests', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('facebook', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(related_name='my_profile', unique=True, to=orm['auth.User'])),
            ('mugshot', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('tele1', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('privacy', self.gf('django.db.models.fields.CharField')(default='registered', max_length=15)),
            ('age', self.gf('django.db.models.fields.CharField')(max_length=3, blank=True)),
            ('tele2', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length='150', blank=True)),
        ))
        db.send_create_signal('users', ['MyProfile'])

        # Deleting model 'UserProfile'
        db.delete_table('users_userprofile')

        # Adding M2M table for field members on 'Team'
        db.create_table('users_team_members', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('team', models.ForeignKey(orm['users.team'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('users_team_members', ['team_id', 'user_id'])


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'users.city': {
            'Meta': {'object_name': 'City'},
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'governorate': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['users.Governorate']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Cairo'", 'max_length': '30'})
        },
        'users.country': {
            'Meta': {'object_name': 'Country'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Egypt'", 'max_length': '30'})
        },
        'users.governorate': {
            'Meta': {'object_name': 'Governorate'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['users.Country']"}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'users.team': {
            'Meta': {'object_name': 'Team'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['users.City']"}),
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'users.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'age': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'gender': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interests': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'monthly_payment': ('django.db.models.fields.DecimalField', [], {'default': '50', 'max_digits': '10', 'decimal_places': '1'}),
            'mugshot': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'myteam': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['users.Team']"}),
            'privacy': ('django.db.models.fields.CharField', [], {'default': "'registered'", 'max_length': '15'}),
            'tele2': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'my_profile'", 'unique': 'True', 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['users']
