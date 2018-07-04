from django.conf.urls import url
from django.contrib import admin

from .views import (
	UserDetailView,
	UserListView,
	)

urlpatterns = [
	url(r'^(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(), name='detail'),
	url(r'^$', UserListView.as_view(), name='list'),

]