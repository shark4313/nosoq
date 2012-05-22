from django.db import models
from userena.models import UserenaBaseProfile
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from datetime import datetime
from easy_thumbnails.fields import ThumbnailerField
from django.contrib.auth.models import User


#class Country(models.Model):
#    name = models.CharField(_('Name'),  max_length=30 , default= "Egypt")
#    class Meta:
#        verbose_name        = _('Country')
#        verbose_name_plural = _('Countries')
#
#    def __unicode__(self):
#        return self.name

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
    MORAL_PREPARATION = 0
    PHYSICAL_PREPARATION = 1
    TRAVELING_DAY = 2
    IHRAM_HOW = 3
    IHRAM_TABOO = 4
    ENTERING_MEKKA = 5
    CATEGORIES = (
                  (MORAL_PREPARATION, _('moral preparation')),
                  (PHYSICAL_PREPARATION , _('physical preparation')),
                  (TRAVELING_DAY , _('traveling day')),
                  (IHRAM_HOW , _('ihram how')),
                  (IHRAM_TABOO , _('ihram taboo')),
                  (ENTERING_MEKKA , _('entering mekka')),
                  )
    BOTH = 0
    MALE = 1
    FEMALE = 2
    WHOM = (
            (BOTH, _('both')),
            (MALE, _('male')),
            (FEMALE, _('female')),
            )
    NOT_DEFINED = 0
    EIGHTH = 1
    NINTH = 2
    TENTH = 3
    ELEVNTH = 4
    TWELVTH = 5
    THIRTEENTH = 6
    DAYS = (
            (NOT_DEFINED, _('not defined')),
            (EIGHTH, _('egihth')),
            (NINTH, _('ninth')),
            (TENTH, _('tenth')),
            (ELEVNTH, _('eleventh')),
            (TWELVTH, _('twelvth')),
            (THIRTEENTH, _('thirteenth')),
            )
    
    title = models.CharField(_('title'), max_length=60, db_index=True)
    message = models.TextField(_("Message"), max_length=1023,  help_text=_("Message sent to the person"))
#    time = models.DateTimeField(_("Time"), help_text=_("When to send this message") , default=datetime.now())
    category = models.IntegerField(_('category'), help_text=('it is relative to manasek start date'), choices=CATEGORIES)
    which_day = models.IntegerField(_('which day'), choices=DAYS)
    for_whom = models.IntegerField(_('for whom'), choices=WHOM, default=BOTH)
    time_interval = models.IntegerField(_('time interval in hours'), help_text=_('it depends on the category chosen'), null=True)
    lon = models.FloatField(_('longitude'), null=True, blank=True)
    lat = models.FloatField(_('latitude'), null=True, blank=True)
    
    class Meta:
        verbose_name = _('notification')
        verbose_name_plural = _('notifications')
    
    def __unicode__(self):
        return self.title
    
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
    GENDER = (
              (MALE, _('male')),
              (FEMALE, _('female')),
            )
    UMRAH = 0
    HAJJ_MUFRED = 1
    HAJJ_QAREN = 2
    HAJJ_MUTAMATE3 = 3
    MANASEK = (
               (UMRAH, _('umrah')),
               (HAJJ_MUFRED, _('hajj mufred')),
               (HAJJ_QAREN, _('hajj qaren')),
               (HAJJ_MUTAMATE3, _('hajj mutamate3')),
               )
    TENTH = 3
    ELEVNTH = 4
    TWELVTH = 5
    THIRTEENTH = 6
    DAYS = (
            (TENTH, _('tenth')),
            (ELEVNTH, _('eleventh')),
            (TWELVTH, _('twelvth')),
            (THIRTEENTH, _('thirteenth')),
            )
    user = models.OneToOneField(User, unique=True, verbose_name=_('user'), related_name='my_profile')
    current_time = models.DateTimeField(_("Current time"), help_text=_("Created in"), default=datetime.now(), editable=False)
    gender = models.IntegerField(_("Gender"), choices=GENDER, default=MALE)
#    location = models.CharField(_("Location"), max_length = 255, blank=True)
    time_to_travel = models.DateTimeField(_('time to travel'), blank=True, null=True)
    manasek_start_date = models.DateField(_('time to start manasek'), blank=True, null=True)
    type_of_mansak = models.IntegerField(_('mansak type'), choices=MANASEK)
    tahallol_day = models.IntegerField(_('tahallol day'), help_text=_('which day to do the great tahallol'), choices=DAYS, blank=True)
    mota3agel = models.BooleanField(_('mot3agel'), blank=True)
    sa3ayt = models.BooleanField(help_text=_('in case you are doing hajj_qeran, did you "sa3ayt" just after umrah'))
    
    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

    def __unicode__(self):
        return ("%s %s") % (self.user.first_name, self.user.last_name)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

    
    
    
    
    
    
    
    
    
