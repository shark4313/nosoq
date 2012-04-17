from SimpleXMLRPCServer import SimpleXMLRPCDispatcher
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.sessions.backends.db import Session
from models import Notification

class XMLRPC(object):
    
    def __init__(self, request):
        self.request = request
    

    def get_notifications(self):
        notifications = Notification.objects.all()
        if notifications:
            from django.forms.models import model_to_dict
            reformed_notifications = []
            for notification in notifications:
                notification = model_to_dict(notification)
                notification.pop('id')
                reformed_notifications.append(notification)
            return reformed_notifications
        else:
            return 'no more notifications'

    def login(self, username, password):
#        if self.request.session.test_cookie_worked():
#            return 'it is working'
        user = auth.authenticate(username=username, password=password)
        if user: auth.login(self.request, user) 
        else: return 'username or password is wrong'
#        SESSION_KEY = '_auth_user_id'
        return self.request.session.session_key

    def get_id_from_session(self, token):
        s = Session.objects.get(session_key=token)
        id = s.get_decoded()['_auth_user_id']
        return id

    def handle_request(self, token):
        self.request.session.session_key = token
        return self.request.user


dispatchers = {}

@csrf_exempt
def xmlrpc_handler(request):
#    try:
#        dispatcher = dispatchers[]
#    except KeyError:
    dispatcher = SimpleXMLRPCDispatcher(encoding=u'UTF-8', allow_none=True)
    dispatcher.register_instance(XMLRPC(request))
#        dispatchers[something] = dispatcher
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
