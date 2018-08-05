from django.conf.urls import url
from django.contrib import admin

from .views import (
	UserDetailView,
	UserListView,
	user_delete,
	profile_update,
	)

urlpatterns = [
	url(r'^(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(), name='detail'),
	url(r'^(?P<username>[\w.@+-]+)/delete$', user_delete, name='profile-delete'),
	url(r'^(?P<username>[\w.@+-]+)/edit$', profile_update, name='profile-delete'),
	url(r'^$', UserListView.as_view(), name='list'),

]