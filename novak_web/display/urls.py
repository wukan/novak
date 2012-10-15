from django.conf.urls import patterns, include, url

urlpatterns = patterns('display.views',
    url(r'^$', 'index'),
    url(r'^(?P<route_id>\w+)/$', 'detail'),
)
