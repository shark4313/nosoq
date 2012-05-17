from SimpleXMLRPCServer import SimpleXMLRPCDispatcher

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from models import News
from generic.functions import queryset_to_list_of_dicts, get_id_from_session
from generic.webservices import ServicesRoot

dispatcher = SimpleXMLRPCDispatcher(allow_none=False, encoding=None) 


class Services(ServicesRoot):
    
    def get_news_by_id(self, id):
        ''' params (token, id) '''
        try:
            news_item = News.objects.get(id=id)
            return news_item
        except News.DoesNotExist:
            return 'no such piece of news'
    
    def get_news_by_date(self, after_date):
        ''' params (token, after_date) '''
        from datetime import date
        after_date = date(after_date[0], after_date[1], after_date[2])
        news = News.objects.filter(date__gte=after_date)
        reformed_news = queryset_to_list_of_dicts(news)
        if reformed_news: 
            return reformed_news
        else:
            return 'no notifications after this date'
    
<<<<<<< HEAD

def get_news_by_id(id , token=None ):

    ''' params (token, id) '''
    try:
        news_item = News.objects.get(id=id)
        return news_item
#        from django.forms.models import model_to_dict
#        news_item = model_to_dict(news_item)
    except News.DoesNotExist:
        return 'no such piece of news'


def get_news_by_location(lon, lat, delta):
    ''' params (lon, lat, delta) '''
    news = News.objects.filter(lon__gt=(lon - delta))
    news = news.filter(lat__gt=(lat - delta))
    news = news.filter(lon__lt=(lon + delta))
    news = news.filter(lat__lt=(lat + delta))
    if news:
        from django.forms.models import model_to_dict
        reformed_news = []
        for news_item in news:
            news_item = model_to_dict(news_item)
            news_item.pop('id')
            reformed_news.append(news_item)
        return reformed_news
    else:
        return 'no more news in this area'

def get_news_by_date(after_date, token=None):

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
dispatcher.register_function(get_news_by_location, 'get_news_by_location')
=======
    def get_news_by_location(self, lon, lat, delta):
        ''' params (lon, lat, delta) '''
        news = News.objects.filter(lon__gt=(lon - delta))
        news = news.filter(lat__gt=(lat - delta))
        news = news.filter(lon__lt=(lon + delta))
        news = news.filter(lat__lt=(lat + delta))
        reformed_news = queryset_to_list_of_dicts(news)
        if reformed_news:
            return reformed_news
        else:
            return 'no more news in this area'

dispatcher.register_instance(Services())

#@csrf_exempt
#def rpc_handler(request, token=None):
#    """
#    the actual handler:
#    if you setup your urls.py properly, all calls to the xml-rpc service
#    should be routed through here.
#    If post data is defined, it assumes it's XML-RPC and tries to process as such
#    Empty post assumes you're viewing from a browser and tells you about the service.
#    """
#    
#    if len(request.POST):
#        id = get_id_from_session(token)
#        if id:
#            response = HttpResponse(mimetype="application/xml")
#            response.write(dispatcher._marshaled_dispatch(request.raw_post_data))
#        else:
#            import xmlrpclib
#            msg = ('token is invalid',)
#            msg = xmlrpclib.dumps(msg, methodresponse=1, allow_none=False, encoding=u'UTF-8')
#            return HttpResponse(msg)            
#    else:
#            response = HttpResponse()
#            response.write("<b>This is an XML-RPC Service.</b><br>")
#            response.write("You need to invoke it using an XML-RPC Client!<br>")
#            response.write("The following methods are available:<ul>")
#            methods = dispatcher.system_listMethods()
#
#            for method in methods:
#                    # right now, my version of SimpleXMLRPCDispatcher always
#                    # returns "signatures not supported"... :(
#                    # but, in an ideal world it will tell users what args are expected
##                        sig = dispatcher.system_methodSignature(method)
#
#                    # this just reads your docblock, so fill it in!
#                    help =  dispatcher.system_methodHelp(method)
#
#                    response.write("<li><b>%s</b>: %s" % (method, help))
#
#            response.write("</ul>")
##                response.write('<a href="http://www.djangoproject.com/"> <img src="http://media.djangoproject.com/img/badges/djangomade124x25_grey.gif" border="0" alt="Made with Django." title="Made with Django."></a>')
#
#    response['Content-length'] = str(len(response.content))
#    return response
    
>>>>>>> c11c6bf31cf8e77beadc20334d79da56d5df3b5b
