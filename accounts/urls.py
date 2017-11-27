from django.conf.urls import url
from django.contrib import admin

from .views import (
	UserDetailView,
	)

urlpatterns = [
	url(r'^(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(), name='detail'),

]