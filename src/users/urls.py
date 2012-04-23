from django.conf.urls.defaults import patterns, include, url
from xmlrpc_webservices import *
    
urlpatterns = patterns('',    
                        url(r'^xmlrpc/login/$', login_handler),
                        url(r'^xmlrpc/call/(.+)$', xmlrpc_handler),
                        url(r'^xmlrpc/register/(.+)$', handle_requests_need_id),
#                        url(r'^xmlrpc/$', xmlrpc_handler),
                        )