from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from xmlrpc_webservices import dispatcher
from generic.xmlrpc_decorator import requires_login

@csrf_exempt
@requires_login(dispatcher)
def xmlrpc_handler(request, token):
    if len(request.POST):
        response = HttpResponse(dispatcher._marshaled_dispatch(request.raw_post_data))
    response = HttpResponse()
    response.write('xmlrpc service')
    return response
#    else:
#        response = HttpResponse()
#        response.write("<b>This is an XML-RPC Service.</b><br>")
#        response.write("You need to invoke it using an XML-RPC Client!<br>")
#        response.write("The following methods are available:<ul>")
#        methods = dispatcher.system_listMethods()
#    
#        for method in methods:
#                # right now, my version of SimpleXMLRPCDispatcher always
#                # returns "signatures not supported"... :(
#                # but, in an ideal world it will tell users what args are expected
#    #                        sig = dispatcher.system_methodSignature(method)
#    
#                # this just reads your docblock, so fill it in!
#                help =  dispatcher.system_methodHelp(method)
#    
#                response.write("<li><b>%s</b>: %s" % (method, help))
#    return response

