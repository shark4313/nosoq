from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from xmlrpc_webservices import dispatcher
from generic.xmlrpc_decorator import requires_login

@csrf_exempt
@requires_login(dispatcher)
def xmlrpc_handler(request, token):
    if len(request.POST):
        response = HttpResponse(dispatcher._marshaled_dispatch(request.raw_post_data))
        return response
    response = HttpResponse()
    response.write('xmlrpc service')
    return response
    