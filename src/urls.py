from django.conf.urls.defaults import patterns, include, url
from userena import views as userena_views
from userena.forms import mSignupForm
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nosoq.views.home', name='home'),
    # url(r'^nosoq/', include('nosoq.foo.urls')),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    
    # Uncomment the next line to enable the admin:
    (r'^accounts/', include('userena.urls')),
    
    url(r'/admintools/', include('admin_tools.urls')),

    url(r'^admin/', include(admin.site.urls)),

        url(r'^$',
    userena_views.signup,
    {'signup_form': mSignupForm}),
    
    )
urlpatterns += staticfiles_urlpatterns()
