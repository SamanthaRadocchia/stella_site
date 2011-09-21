"""The main urls configuration file. Delegates app-specific urls to those
apps' urls confs.
"""

from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.contrib import admin

admin.autodiscover() # enables admin

# Examples:
# url(r'^$', 'stella_project.views.home', name='home'),
# url(r'^stella_project/', include('stella_project.foo.urls')),

urlpatterns = patterns('',
                       # admin documentation
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       # admin
                       url(r'^admin/', include(admin.site.urls)),
                       # main
                       url(r'^$', direct_to_template, template="main.html"),
                       # user accounts
                       url(r'^accounts/', include(users.urls)),
                       )