from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

class News(models.Model):
    title = models.CharField(_('title'), max_length=60)
    body = models.TextField(_('conetent'))
    date = models.DateTimeField(_('date'))
    lon = models.FloatField(_('longitude'))
    lat = models.FloatField(_('latitude'))
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name = _('news item')
        verbose_name_plural = _('news')
        
        
class Registrant(models.Model):
    user = models.OneToOneField(User)
    
    def __unicode(self):
        return self.user
    
    class Meta:
        verbose_name = _('registrant')
        verbose_name_plural = _('registrants')