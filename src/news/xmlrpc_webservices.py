# Patchless XMLRPC Service for Django
# Kind of hacky, and stolen from Crast on irc.freenode.net:#django
# Self documents as well, so if you call it from outside of an XML-RPC Client
# it tells you about itself and its methods
#
# Brendan W. McAdams <brendan.mcadams@thewintergrp.com>

# SimpleXMLRPCDispatcher lets us register xml-rpc calls w/o
# running a full XMLRPC Server.  It's up to us to dispatch data

from SimpleXMLRPCServer import SimpleXMLRPCDispatcher
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from models import News
# Create a Dispatcher; this handles the calls and translates info to function maps
#dispatcher = SimpleXMLRPCDispatcher() # Python 2.4
dispatcher = SimpleXMLRPCDispatcher(allow_none=False, encoding=None) # Python 2.5

 
@csrf_exempt
def rpc_handler(request):
        """
        the actual handler:
        if you setup your urls.py properly, all calls to the xml-rpc service
        should be routed through here.
        If post data is defined, it assumes it's XML-RPC and tries to process as such
        Empty post assumes you're viewing from a browser and tells you about the service.
        """

        if len(request.POST):
                response = HttpResponse(mimetype="application/xml")
                response.write(dispatcher._marshaled_dispatch(request.raw_post_data))
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
#                        sig = dispatcher.system_methodSignature(method)

                        # this just reads your docblock, so fill it in!
                        help =  dispatcher.system_methodHelp(method)

                        response.write("<li><b>%s</b>: %s" % (method, help))

                response.write("</ul>")
#                response.write('<a href="http://www.djangoproject.com/"> <img src="http://media.djangoproject.com/img/badges/djangomade124x25_grey.gif" border="0" alt="Made with Django." title="Made with Django."></a>')

        response['Content-length'] = str(len(response.content))
        return response


def multiply(a, b):
        """
        Multiplication is fun!
        Takes two arguments, which are multiplied together.
        Returns the result of the multiplication!
        """

        return int(a) * int(b) 
    

def get_news_by_id(token, id):
    ''' params (token, id) '''
    try:
        news_item = News.objects.get(id=id)
        return news_item
#        from django.forms.models import model_to_dict
#        news_item = model_to_dict(news_item)
    except News.DoesNotExist:
        return 'no such piece of news'


def get_news_by_date(token, after_date):
    ''' params (token, after_date) '''
    from datetime import date
    after_date = date(after_date[0], after_date[1], after_date[2])
    news = News.objects.filter(date__gte=after_date)
    if news:
        from django.forms.models import model_to_dict
        reformed_news = []
        for news_item in news:
            news_item = model_to_dict(news_item)
            news_item.pop('id')
            reformed_news.append(news_item)
        return reformed_news
    else:
        return 'no notifications after this date'
# you have to manually register all functions that are xml-rpc-able with the dispatcher
# the dispatcher then maps the args down.
# The first argument is the actual method, the second is what to call it from the XML-RPC side...
dispatcher.register_function(get_news_by_date, 'get_news_by_date')
dispatcher.register_function(get_news_by_id, 'get_news_by_id')
