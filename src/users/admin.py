'''
Created on Nov 9, 2011

@author: Alsayed Gamal
'''

from django.utils.translation import ugettext as _
from users.models import *

from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class NotificationAdmin(admin.ModelAdmin):
    model = Notification
    list_display = ('title', 'category', 'which_day', 'for_whom')
    list_editable = ('category', 'which_day', 'for_whom')

#admin.site.register(Country)
admin.site.register(UserProfile)
admin.site.register(Media)
admin.site.register(Notification, NotificationAdmin)
