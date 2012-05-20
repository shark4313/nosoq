from django.conf.urls.defaults import patterns, url
from views import xmlrpc_handler

urlpatterns = patterns('',
                       url(r'^call/(.+)$', xmlrpc_handler),
                       )