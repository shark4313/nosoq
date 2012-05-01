from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from xmlrpc_webservices import dispatcher
from generic.xmlrpc_decorator import requires_login
from users.forms import *

#ajax request 
def feed_models(request, city_id):    
    city = City.objects.get(pk=city_id)  
    teams = Team.objects.filter(city=city)     
    return render_to_response('teamSelection.html', {"city_id":city_id,'teams':teams}, )

def handle(request):
    if request.method == 'POST':
         artists = request.POST.getlist('artists') 
         # now artists is a list of [1,2,3]

         
def add_classified(request):
    form = MyForm()
    if request.method == 'POST':
        form = MyForm(request.POST)
    if request.POST.has_key('city'):
        model_id = request.POST['city']
    else:
        model_id = 0
    return render_to_response('test.html', {'form':form,'model_id':model_id}, context_instance=RequestContext(request))


@csrf_exempt
@requires_login(dispatcher)
def xmlrpc_handler(request, token):
    if len(request.POST):
        response = HttpResponse(dispatcher._marshaled_dispatch(request.raw_post_data))
        return response
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
#                help =  dispatcher.system_methodHelp(method)
#                response.write("<li><b>%s</b>: %s" % (method, help))
#    return response 

@csrf_exempt
def token_checker(request):
    if len(request.POST):
        response = HttpResponse(dispatcher._marshaled_dispatch(request.raw_post_data))
        return response
    response = HttpResponse()
    response.write('xmlrpc service')
    return response

@csrf_exempt
def login_handler(request):
    if len(request.POST):
        response = HttpResponse(dispatcher._marshaled_dispatch(request.raw_post_data))
    else:
        response = HttpResponse('this is the login url')
    return response


