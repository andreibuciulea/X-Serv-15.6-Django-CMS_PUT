from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^logout$', "django.contrib.auth.views.logout"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', "sitios.views.lugares"),
    url(r'^sitio/(.*)$', "sitios.views.info"),
    url(r'^(.*)$', "sitios.views.notfound")
)
