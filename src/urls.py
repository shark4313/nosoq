from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

from userena import views as userena_views
from userena.forms import mSignupForm
from linaro_django_xmlrpc import urls

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^accounts/', include('userena.urls')),
    url(r'/admintools/', include('admin_tools.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', userena_views.signup, {'signup_form': mSignupForm}),
    url(r'^news/', include('news.urls')),
    url(r'^users/', include('users.urls')),
    )

urlpatterns += staticfiles_urlpatterns()
