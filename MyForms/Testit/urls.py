#from django.conf.urls import patterns, include, url
#from hello.views import foo
#from django.conf.urls import *
#from django.contrib import admin
#admin.autodiscover()
from django.conf.urls import url
from django.shortcuts import render
from django.contrib import admin
from . import views


urlpatterns=[
    # Examples:
    # url(r'^$', 'HelloWorld.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.hello, name='hello'),
    url(r'^index$', views.index, name='index'),
    url(r'^Page1$', views.Page1, name='Page1'),
    #url(r'^hell$', views.hell,name='hello'),
    #url(r'^post_list$', views.post_list,name='post_list'),
    #url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    #url(r'^post/new/$', views.post_new, name='post_new'),
    #url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    #url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    #url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    #url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    #url(r'^admin/', admin.site.urls)
]
