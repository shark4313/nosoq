import xmlrpclib

from django.http import HttpResponse

from generic.functions import get_id_from_session
#from xmlrpc_webservices import dispatcher

def requires_login(dispatcher):
    def _view_receiver(view):
        def _check_token(*args, **kwargs):
#            if len(args[0].POST):
            id = get_id_from_session(args[1])
            if id:
                dispatcher.instance.user_id = id
                response = view(*args, **kwargs)
            else:
                msg = ('token is invalid',)
                msg = xmlrpclib.dumps(msg, methodresponse=1, allow_none=False, encoding=u'UTF-8')
                response = HttpResponse(msg)
            return response
#            else:
#                response = view(*args, **kwargs)
        return _check_token
    return _view_receiver
