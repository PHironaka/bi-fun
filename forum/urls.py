from django.conf.urls import url
from django.contrib import admin

from .views import (
	forum_list,
	forum_create,
	forum_detail,
	forum_update,
	forum_delete,
	forumLikeToggle,
	forumLikeAPIToggle,
	)

urlpatterns = [
	url(r'^$', forum_list, name='list'),
    url(r'^create/$', forum_create, name='create'),
    url(r'^(?P<slug>[\w-]+)/$', forum_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/like/$', forumLikeToggle.as_view(), name='like-toggle'),
    url(r'^api/(?P<slug>[\w-]+)/like/$', forumLikeAPIToggle.as_view(), name='like-api-toggle'),
    url(r'^(?P<slug>[\w-]+)/edit/$', forum_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', forum_delete),

    #url(r'^posts/$', "<appname>.views.<function_name>"),
]