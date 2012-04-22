'''
Created on Nov 9, 2011

@author: Alsayed Gamal
'''

from django.utils.translation import ugettext as _
from users.models import *

from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User




#admin.site.register(Country)
admin.site.register(UserProfile)
admin.site.register(Media)
admin.site.register(Notification)
