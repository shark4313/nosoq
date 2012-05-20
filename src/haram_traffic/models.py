from django.contrib.gis.db import models
from django.utils.translation import ugettext as _

class TrafficStatus(models.Model):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    STATES = (
              (LOW, _('low')),
              (MEDIUM, _('medium')),
              (HIGH, _('high')),
              )
    lon = models.FloatField()
    lat = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)
    value = models.IntegerField(choices=STATES)
    
    objects = models.GeoManager()
    
    class Meta:
        verbose_name = _('state')
        verbose_name_plural = _('states')
