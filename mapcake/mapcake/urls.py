from django.conf.urls import patterns, include, url
from django.contrib.gis import admin
from layers import views

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^layers/add', views.layer_add, name='add'),
    url(r'^layers/index', views.layer_index, name='layer_index'),
    url(r'^layers/(?P<source_id>\d+)/delete', views.layer_delete, name='source_delete'),
    # ex: /polls/5/
    url(r'^layers/(?P<source_id>\d+)/$', views.layer_detail,
        name='source_detail'),
    ## (r'^layers/$', 'mapcake.views.index'),
   ## (r'^layers/(?P<poll_id>\d+)/$', 'mapcake.views.detail'),
   ## (r'^layers/(?P<poll_id>\d+)/results/$', 'mapcake.views.results'),
   ## (r'^layers/(?P<poll_id>\d+)/vote/$', 'mapcake.views.vote'),
    (r'^admin/', include(admin.site.urls)),
    (r'^account/', include('userena.urls')), 
    url(r'^$', include('home.urls')), 
)
