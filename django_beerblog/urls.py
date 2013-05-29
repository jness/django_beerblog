from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    # Our Views
    url(r'^$', 'beerblog.views.home', name='home'),
    url(r'^beers/$', 'beerblog.views.beers', name='beers'),
    url(r'^wines/$', 'beerblog.views.wines', name='wines'),
)
