from SimpleXMLRPCServer import SimpleXMLRPCDispatcher

from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from models import Notification
from generic.functions import queryset_to_list_of_dicts, get_id_from_session

dispatcher = SimpleXMLRPCDispatcher(encoding=u'UTF-8', allow_none=True)

@csrf_exempt
def xmlrpc_handler(request, token=None):
    if len(request.POST):
        id = get_id_from_session(token)
        if id:
            return HttpResponse(dispatcher._marshaled_dispatch(request.raw_post_data))
        else:
            import xmlrpclib
            msg = ('token is invalid',)
            msg = xmlrpclib.dumps(msg, methodresponse=1, allow_none=False, encoding=u'UTF-8')
            return HttpResponse(msg)
    else:
        response = HttpResponse()
        response.write("<b>This is an XML-RPC Service.</b><br>")
        response.write("You need to invoke it using an XML-RPC Client!<br>")
        response.write("The following methods are available:<ul>")
        methods = dispatcher.system_listMethods()

        for method in methods:
                # right now, my version of SimpleXMLRPCDispatcher always
                # returns "signatures not supported"... :(
                # but, in an ideal world it will tell users what args are expected
#                sig = dispatcher.system_methodSignature(method)

                # this just reads your docblock, so fill it in!
                help =  dispatcher.system_methodHelp(method)

                response.write("<li><b>%s</b>: %s" % (method, help))

        response.write("</ul>")
#        response.write('<a href="http://www.djangoproject.com/"> <img src="http://media.djangoproject.com/img/badges/djangomade124x25_grey.gif" border="0" alt="Made with Django." title="Made with Django."></a>')
        response['Content-length'] = str(len(response.content))
        return response


@csrf_exempt
def login_handler(request):
    dispatcher.register_instance(Authentication(request))
    if len(request.POST):
        return HttpResponse(dispatcher._marshaled_dispatch(request.raw_post_data))

class Authentication(object):
    def __init__(self, request):
        self.request = request
        
    def login(self, username, password):
        ''' params (username, password) '''
        user = auth.authenticate(username=username, password=password)
        if user: auth.login(self.request, user) 
        else: return 'username or password is wrong'
        return self.request.session.session_key

def get_notifications_by_id(id):
    ''' params (token : String, id : integer) '''
    try:
        notification = Notification.objects.get(id=id)
        from django.forms.models import model_to_dict
        notification = model_to_dict(notification)
        return notification
    except Notification.DoesNotExist:
        return 'no such notification'

def get_notifications_by_date(after_date):
    ''' params (token : String, after_date : list[year, month, day]) '''
    from datetime import datetime
    after_date = datetime(after_date[0], after_date[1], after_date[2])
    notifications = Notification.objects.filter(time__gte=after_date)
    reformed_notifications = queryset_to_list_of_dicts(notifications)
    if reformed_notifications:
        return reformed_notifications
    else:
        return 'no notifications after this date'

def get_notifications_by_location(lon, lat, delta):
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

dispatcher.register_function(get_notifications_by_id)
dispatcher.register_function(get_notifications_by_date)
dispatcher.register_function(get_notifications_by_location)

class IdDependentServices(object):
    
    def __init__(self, id):
        self.id = id
            
    def register_to_app(self, app_name):
        ''' params (app_name) '''
        if app_name == 'news':
            from src.news.models import Registrant
            Registrant.objects.create(user=User.objects.get(id=self.id))
            return 'app has been registered'


@csrf_exempt
def handle_requests_need_id(request, token):
    dispatcher = SimpleXMLRPCDispatcher(encoding=u'UTF-8', allow_none=True)
    if len(request.POST):
        id = get_id_from_session(token)
        if id:
            dispatcher.register_instance(IdDependentServices(id))
            return HttpResponse(dispatcher._marshaled_dispatch(request.raw_post_data))
        else:
            import xmlrpclib
            msg = ('token is invalid',)
            msg = xmlrpclib.dumps(msg, methodresponse=1, allow_none=False, encoding=u'UTF-8')
            return HttpResponse(msg)
    else:
        response = HttpResponse()
        response.write("<b>This is an XML-RPC Service.</b><br>")
        response.write("You need to invoke it using an XML-RPC Client!<br>")
        response.write("The following methods are available:<ul>")
        methods = dispatcher.system_listMethods()

        for method in methods:
                # right now, my version of SimpleXMLRPCDispatcher always
                # returns "signatures not supported"... :(
                # but, in an ideal world it will tell users what args are expected
#                sig = dispatcher.system_methodSignature(method)

                # this just reads your docblock, so fill it in!
                help =  dispatcher.system_methodHelp(method)

                response.write("<li><b>%s</b>: %s" % (method, help))

        response.write("</ul>")
#        response.write('<a href="http://www.djangoproject.com/"> <img src="http://media.djangoproject.com/img/badges/djangomade124x25_grey.gif" border="0" alt="Made with Django." title="Made with Django."></a>')
        response['Content-length'] = str(len(response.content))
        return response

