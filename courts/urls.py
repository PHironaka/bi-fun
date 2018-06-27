from django.conf.urls import url
from django.contrib import admin

from .views import (
	court_list,
	court_create,
	court_detail,
	court_update,
	court_delete,
	courtLikeToggle,
	courtLikeAPIToggle,
	TagIndexView,

	)

urlpatterns = [
	url(r'^$', court_list, name='list'),
	url(r'^create/$', court_create, name='create'),
	url(r'^courts/(?P<slug>[\w-]+)/edit/$', court_update, name='update'),
	url(r'^courts/(?P<slug>[\w-]+)/delete/$', court_delete, name='delete'),
    url(r'^courts/(?P<slug>[\w-]+)/like/$', courtLikeToggle.as_view(), name='like-toggle'),
    url(r'^courts/(?P<slug>[\w-]+)/api/like/$', courtLikeAPIToggle.as_view(), name='like-api-toggle'),
	url(r'^courts/(?P<slug>[\w-]+)/$', court_detail, name='detail'),
    url(r'^courts/tags/(?P<slug>[\w-]+)/$', TagIndexView.as_view(), name='tag'),


    #url(r'^posts/$', "<appname>.views.<function_name>"),
]