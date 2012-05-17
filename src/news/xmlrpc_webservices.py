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

