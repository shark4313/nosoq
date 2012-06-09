from SimpleXMLRPCServer import SimpleXMLRPCDispatcher

from django.contrib import auth
from django.contrib.auth.models import User

from models import Notification
from generic.functions import queryset_to_list_of_dicts
from generic.webservices import ServicesRoot

dispatcher = SimpleXMLRPCDispatcher(encoding=u'UTF-8', allow_none=True)

class Services(ServicesRoot):
    
    def get_notifications_by_id(self, id):
        ''' params (token : String, id : integer) '''
        try:
            notification = Notification.objects.get(id=id)
            from django.forms.models import model_to_dict
            notification = model_to_dict(notification)
            return notification
        except Notification.DoesNotExist:
            return 'no such notification'
    
    def get_notifications_by_date(self, after_date):
        ''' params (token : String, after_date : list[year, month, day]) '''
        from datetime import datetime
        after_date = datetime(after_date[0], after_date[1], after_date[2])
        notifications = Notification.objects.filter(time_interval__gte=after_date)
        reformed_notifications = queryset_to_list_of_dicts(notifications)
        if reformed_notifications:
            return reformed_notifications
        else:
            return 'no notifications after this date'
  
#    def get_notifications_by_timeInterval(self, category, timeInterval):

    def get_notifications_by_filters(self, kwargs):
        ''' params (token : String, kwargs : dict) '''
        notifications = Notification.objects.filter(**kwargs)
        reformed_notifications = queryset_to_list_of_dicts(notifications)
        if reformed_notifications:
            return reformed_notifications
        else:
            return 'no notifications'

    def get_notifications_by_for_whom(self, for_whom):
        ''' params (token : String, for_whom :Integer) '''
        notifications = Notification.objects.filter(for_whom=for_whom)
        reformed_notifications = queryset_to_list_of_dicts(notifications)
        if reformed_notifications:
            return reformed_notifications
        else:
            return 'no notifications'

    def get_notifications_by_category(self, category):
        ''' params (token : String, category_name :Integer) '''
        notifications = Notification.objects.filter(category=category)
        reformed_notifications = queryset_to_list_of_dicts(notifications)
        if reformed_notifications:
            return reformed_notifications
        else:
            return 'no notifications'

    def get_notifications_by_which_day(self, which_day):
        ''' params (token : String, which_day :Integer) '''
        notifications = Notification.objects.filter(which_day=which_day)
        reformed_notifications = queryset_to_list_of_dicts(notifications)
        if reformed_notifications:
            return reformed_notifications
        else:
            return 'no notifications'

    def get_notifications_by_date2(self, after_date_year,after_date_month,after_date_day):
        ''' params (token : String, after_date : list[year, month, day]) '''
        from datetime import datetime
        after_date = datetime(after_date_year, after_date_month, after_date_day)
        notifications = Notification.objects.filter(time__gte=after_date)
        reformed_notifications = queryset_to_list_of_dicts(notifications)
        if reformed_notifications:
            return reformed_notifications
        else:
            return 'no notifications after this date'

 
    def get_notifications_by_location(self, lon, lat, delta):
        ''' params (lon, lat, delta) '''
        notifications = Notification.objects.filter(lon__gt=(lon - delta))
        notifications = notifications.filter(lat__gt=(lat - delta))
        notifications = notifications.filter(lon__lt=(lon + delta))
        notifications = notifications.filter(lat__lt=(lat + delta))
        reformed_notifications = queryset_to_list_of_dicts(notifications)
        if reformed_notifications:
            return reformed_notifications
        else:
            return 'no notifications in this area'
    
    def register_to_app(self, app_name):
        ''' params (app_name) '''
        from django.conf import settings
        if app_name in settings.AVAILABLE_APPS:
            from django.db.models import get_app
            app = get_app(app_name)
            model = app.Registrant
            try:
                model.objects.create(user=User.objects.get(id=self.user_id))
                msg = 'app has been registered'
            except:
                msg = 'you are already registered to %s' % app_name
            return msg
        return 'no such app'
    
        
def token_is_valid(token):
    from django.contrib.sessions.backends.db import Session
    try:
        Session.objects.get(session_key=token)
        return True
    except Session.DoesNotExist:
        return False


def login(username, password):
    ''' params (username, password) '''
    from django.contrib.sessions.backends.db import SessionStore
    user = auth.authenticate(username=username, password=password)
    if user: 
        session = SessionStore()
        session['user_id'] = user.id
        session.save()
        response = session.session_key
    else: 
        response = 'username or password is wrong'
    return response

dispatcher.register_instance(Services())
dispatcher.register_function(login)
dispatcher.register_function(token_is_valid)
#dispatcher.register_function(get_notifications_by_id)
#dispatcher.register_function(get_notifications_by_date)
#dispatcher.register_function(get_notifications_by_location)
#dispatcher.register_function(register_to_app)

