from django.conf.urls.defaults import patterns, include, url
from xmlrpc_webservices import rpc_handler

urlpatterns = patterns('',
                       (r'^xmlrpc/$', rpc_handler),
                       (r'^xmlrpc/(.+)', rpc_handler),
                       )