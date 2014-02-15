from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mapcake.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', 'home.views.index', name='index'),
    # url(r'^index.html$', include('home.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls', namespace="accounts")),
    url(r'^$', include('home.urls', namespace = "home")),
    url(r'^layers/', include('layers.urls', namespace = "layers")),
)
