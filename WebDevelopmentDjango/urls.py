#!/usr/bin/env python
#  -*- coding: UTF-8 -*-
# vim: set fileencoding=UTF-8 :

from django.conf.urls import include, url
from django.contrib import admin

from .views import MainView

urlpatterns = [
	url(r'^$', MainView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
	# Apps
	url(r'^team/', include('team.urls', namespace='teams')),
	url(r'^members/', include('members.urls', namespace='members')),
]
