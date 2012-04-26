from django.conf.urls.defaults import patterns, include, url
from views import xmlrpc_handler

urlpatterns = patterns('',
                       (r'^xmlrpc/call/(.+)$', xmlrpc_handler),
#                       (r'^xmlrpc/(.+)', rpc_handler),
                       )