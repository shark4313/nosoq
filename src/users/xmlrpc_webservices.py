from SimpleXMLRPCServer import SimpleXMLRPCDispatcher

from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.sessions.backends.db import Session
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from models import Notification
from generic.functions import queryset_to_list_of_dicts

class XMLRPC(object):
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
            


    
dispatchers = {}
@csrf_exempt
def xmlrpc_handler(request, token=None):
    dispatcher = SimpleXMLRPCDispatcher(encoding=u'UTF-8', allow_none=True)
    dispatcher.register_instance(XMLRPC())
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


class Authentication(object):
    def __init__(self, request):
        self.request = request

        
    def login(self, username, password):
        ''' params (username, password) '''
        user = auth.authenticate(username=username, password=password)
        if user: auth.login(self.request, user) 
        else: return 'username or password is wrong'
        return self.request.session.session_key

def get_id_from_session(token):
    try:
        s = Session.objects.get(session_key=token)
        id = s.get_decoded()['_auth_user_id']
        return id
    except Session.DoesNotExist:
        return False

@csrf_exempt
def login_handler(request):
    dispatcher = SimpleXMLRPCDispatcher(encoding=u'UTF-8', allow_none=True)
    dispatcher.register_instance(Authentication(request))
    if len(request.POST):
        return HttpResponse(dispatcher._marshaled_dispatch(request.raw_post_data))


#from SimpleXMLRPCServer import SimpleXMLRPCDispatcher
#from django.views.decorators.http import require_POST
#from django.http import HttpResponse
#
#class XMLRPC(object):
##    def __init__(self, something):
##        self.something  = something
#
#    def do_something(self, *args):
#        # code of exported function here
#        pass
#
#    def mail(self):
#        return 'welcome'
#
##dispatchers = {}
#
#
#dispatcher = SimpleXMLRPCDispatcher(encoding=u'UTF-8', allow_none=True)
#dispatcher.register_instance(XMLRPC())
#
#
#@require_POST
#def xmlrpc2(request):
##    try:
##        dispatcher = dispatchers[something]
##    except KeyError:
##        return HttpResponse(hello)
##        dispatchers[something] = dispatcher
#
#    return HttpResponse(dispatcher._marshaled_dispatch(request.raw_post_data))




# Create a Dispatcher; this handles the calls and translates info to function maps
#dispatcher = SimpleXMLRPCDispatcher() # Python 2.4
#dispatcher = SimpleXMLRPCDispatcher(allow_none=False, encoding=None) # Python 2.5
#
#@csrf_exempt
#def xmlrpc1(request):
#        """
#        the actual handler:
#        if you setup your urls.py properly, all calls to the xml-rpc service
#        should be routed through here.
#        If post data is defined, it assumes it's XML-RPC and tries to process as such
#        Empty post assumes you're viewing from a browser and tells you about the service.
#        """
#
#        if len(request.POST):
#                response = HttpResponse(mimetype="application/xml")
#                response.write(dispatcher._marshaled_dispatch(request.raw_post_data))
#        else:
#                response = HttpResponse()
#                response.write("this is amr negm greeting :)<br>")
#                response.write("<b>This is an XML-RPC Service.</b><br>")
#                response.write("You need to invoke it using an XML-RPC Client!<br>")
#                response.write("The following methods are available:<ul>")
#                methods = dispatcher.system_listMethods()
#
#                for method in methods:
#                        # right now, my version of SimpleXMLRPCDispatcher always
#                        # returns "signatures not supported"... :(
#                        # but, in an ideal world it will tell users what args are expected
#                        sig = dispatcher.system_methodSignature(method)
#
#                        # this just reads your docblock, so fill it in!
#                        help =  dispatcher.system_methodHelp(method)
#
#                        response.write("<li><b>%s</b>: [%s] %s" % (method, sig, help))
#
#                response.write("</ul>")
#                response.write('<a href="http://www.djangoproject.com/"> <img src="http://media.djangoproject.com/img/badges/djangomade124x25_grey.gif" border="0" alt="Made with Django." title="Made with Django."></a>')
#
#        response['Content-length'] = str(len(response.content))
#        return response
#
#
#def multiply(a, b):
#        """
#        Multiplication is fun!
#        Takes two arguments, which are multiplied together.
#        Returns the result of the multiplication!
#        """
#        return a*b
#
## you have to manually register all functions that are xml-rpc-able with the dispatcher
## the dispatcher then maps the args down.
## The first argument is the actual method, the second is what to call it from the XML-RPC side...
#dispatcher.register_function(multiply, 'multiply')
#
#
#def mail():
#        return 'welcome'
#
#dispatcher.register_function(mail, 'mail')

