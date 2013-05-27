from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),

    # Our Views
    url(r'^$', 'beerblog.views.beers', name='beers'),
    url(r'^breweries/$', 'beerblog.views.breweries', name='breweries'),
    url(r'^styles/$', 'beerblog.views.beer_types', name='beer_types'),
)
