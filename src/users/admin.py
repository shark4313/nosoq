from django.utils.translation import ugettext as _
from users.models import *

from django.contrib import admin

class NotificationAdmin(admin.ModelAdmin):
    model = Notification
    list_display = ('title', 'category', 'which_day', 'for_whom')
    list_editable = ('category', 'which_day', 'for_whom')
    list_filter = ('for_whom', 'category', 'which_day')

#admin.site.register(Country)
admin.site.register(UserProfile)
admin.site.register(Media)
admin.site.register(Notification, NotificationAdmin)
