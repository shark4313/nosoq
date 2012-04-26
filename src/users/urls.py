from django.conf.urls.defaults import patterns, include, url
from views import login_handler, xmlrpc_handler

urlpatterns = patterns('',    
                        url(r'^xmlrpc/login/$', login_handler),
                        url(r'^xmlrpc/call/(.+)$', xmlrpc_handler),
#                        url(r'^xmlrpc/register/(.+)$', handle_requests_need_id),
#                        url(r'^xmlrpc/$', xmlrpc_handler),
                        )