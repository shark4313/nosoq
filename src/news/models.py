from django.db import models
from django.utils.translation import ugettext as _

class News(models.Model):
    title = models.CharField(_('title'), max_length=60)
    body = models.TextField(_('conetent'))
    date = models.DateTimeField(_('date'))
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name = _('news item')
        verbose_name_plural = _('news')
        
        