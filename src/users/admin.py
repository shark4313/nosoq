
from django.contrib import admin
from src.users.models import Notification, UserProfile, Media


class NotificationAdmin(admin.ModelAdmin):
    model = Notification
    fields = ('title', 'message', 'title_en', 'message_en', 'category',
              'which_day', 'hajj_type', 'for_whom', 'time_interval',
              'lon', 'lat')
    list_display = ('title', 'category', 'which_day', 'for_whom', 'hajj_type')
    list_editable = ('category', 'hajj_type', 'which_day', 'for_whom')
    list_filter = ('for_whom', 'category', 'which_day')

#admin.site.register(Country)
admin.site.register(UserProfile)
admin.site.register(Media)
admin.site.register(Notification, NotificationAdmin)
