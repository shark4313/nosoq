from django.db import models
from userena.models import UserenaBaseProfile
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from datetime import datetime
from easy_thumbnails.fields import ThumbnailerField
from django.contrib.auth.models import User


class Country(models.Model):
    name = models.CharField(_('Name'),  max_length=30 , default= "Egypt")
    class Meta:
        verbose_name        = _('Country')
        verbose_name_plural = _('Countries')

    def __unicode__(self):
        return self.name

class Media(models.Model):
    
    IMAGE_TYPE = 0
    VIDEO_TYPE = 1
    TYPES = (
                (IMAGE_TYPE, _('image')),
                (VIDEO_TYPE, _('video'))
             )

    type = models.IntegerField(_("Media Type"), max_length=1, choices=TYPES)
    item_name = models.CharField(_("Name"), help_text=_("Media Item name"), max_length=100)
    add_time = models.DateTimeField(_("Time"), help_text=_("Addition time"), default=datetime.now())
    item_file_name = ThumbnailerField(_("File name"), help_text=_("Media item file name"), upload_to="media_items")
    
    def __unicode__(self):
        return self.item_name

    class Meta:
        verbose_name = _('Media Item')
        verbose_name_plural = _('Media Items')

class Notification(models.Model):
    address = models.CharField(max_length=255, db_index=True)
    message = models.TextField(_("Message"), max_length=1023,  help_text=_("Message sent to the person"))
    time = models.DateTimeField(_("Time"), help_text=_("When to send this message") , default=datetime.now())

#class News(models.Model):
#    media =  models.ManyToManyField("Media" , blank=True)
#    header = models.CharField(_("Header") , max_length=255 , blank=True , null= True)
#    description = models.TextField(_("short description"), max_length=255, blank=True, null=True, help_text=_("short description of the image"))
#    pub_date    = models.DateTimeField(_("Created in"),help_text=_("Created in") , default = datetime.now() , editable = False)
#    
#    def __unicode__(self):
#        return self.header
#    
#    class Meta:
#        verbose_name = _('News')
#        verbose_name_plural = _('News')

        
class UserProfile(UserenaBaseProfile):
    MALE= 0
    FEMALE = 1
 
    GENDER_CHOICES = (
               
                (MALE, _('male')),
                (FEMALE, _('female')) ,

            )

    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='my_profile')
    
    current_time    = models.DateTimeField(_("Current time"),help_text=_("Created in") , default = datetime.now() , editable = False)
    
    gender = models.IntegerField(_("Gender"), choices=GENDER_CHOICES, default=MALE)
    location = models.CharField(_("Location") , max_length = 255)

    def __unicode__(self):
        return   ("%s  %s") %( self.user.first_name , self.user.last_name  )

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])