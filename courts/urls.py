from django.conf.urls import url
from django.contrib import admin

from .views import (
	court_list,
	court_create,
	court_detail,
	court_update,
	court_delete,
	)

urlpatterns = [
	url(r'^$', court_list, name='list'),
	url(r'^courts/create/$', court_create, name='create'),
	url(r'^courts/(?P<slug>[\w-]+)/$', court_detail, name='detail'),

    #url(r'^posts/$', "<appname>.views.<function_name>"),
]