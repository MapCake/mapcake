from django.conf.urls import patterns, include, url

from home import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mapcake.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
  )