from django.conf.urls import patterns, include, url
from django.contrib import admin

from layers import views


admin.autodiscover()


urlpatterns = patterns('',
	  # Examples:
    # url(r'^$', 'mapcake.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', 'home.views.index', name='index'),
    # url(r'^index.html$', include('home.urls')),
    url(r'^add/', views.layer_add, name='add'),
    url(r'^$', views.layer_index, name='layer_index'),
    url(r'^(?P<source_id>\d+)/delete', views.layer_delete, name='source_delete'),
    # ex: /polls/5/
    url(r'^(?P<source_id>\d+)/$', views.layer_detail,
        name='source_detail'),
)