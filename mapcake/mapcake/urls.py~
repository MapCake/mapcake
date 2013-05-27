from django.conf.urls import patterns, include, url
from django.contrib.gis import admin
from mapcake import views

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^layers/add', views.layer_add, name='layer_add'),
    url(r'^sources/add', views.source_add, name='add'),
    url(r'^sources/index', views.source_index, name='source_index'),
    url(r'^sources/(?P<source_id>\d+)/delete', views.source_delete, name='source_delete'),
    # ex: /polls/5/
    url(r'^sources/(?P<source_id>\d+)/$', views.source_detail,
        name='source_detail'),
    ## (r'^layers/$', 'mapcake.views.index'),
   ## (r'^layers/(?P<poll_id>\d+)/$', 'mapcake.views.detail'),
   ## (r'^layers/(?P<poll_id>\d+)/results/$', 'mapcake.views.results'),
   ## (r'^layers/(?P<poll_id>\d+)/vote/$', 'mapcake.views.vote'),
    (r'^admin/', include(admin.site.urls)),
)
