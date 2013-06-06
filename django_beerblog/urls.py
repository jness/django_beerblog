from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

# needed when testing dev
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    # Our Views
    url(r'^$', 'beerblog.views.home', name='home'),
    url(r'^beers/$', 'beerblog.views.beers', name='beers'),
    url(r'^beers/(?P<pk>[0-9]+)$', 'beerblog.views.beer', name='beer'),
    url(r'^wines/$', 'beerblog.views.wines', name='wines'),
    url(r'^wines/(?P<pk>[0-9]+)$', 'beerblog.views.wine', name='wine'),
    url(r'^search/$', 'beerblog.views.search', name='search'),
)

# needed when testing in dev
# urlpatterns += staticfiles_urlpatterns()
