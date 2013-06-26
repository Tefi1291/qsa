from django.conf.urls import patterns, include, url
from series.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'django.contrib.auth.views.login', {'template_name': "index.html"}),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', {'login_url': "/"}),
    url(r'^my_profile/$', profile),
    url(r'^about/$', about),
    url(r'^contact/$', contact),


    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
