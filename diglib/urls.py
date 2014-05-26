from django.conf.urls import patterns, url

from diglib import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),
    url(r'^search_results/$', views.search_results, name='search_results'),
)
