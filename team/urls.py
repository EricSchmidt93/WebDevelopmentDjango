#!/usr/bin/env python
#  -*- coding: UTF-8 -*-
# vim: set fileencoding=UTF-8 :

from django.conf.urls import url

from .views import HomeView, TeamView, CreateTeamView, TeamDeleteView

urlpatterns = [
	url(r'^$', HomeView.as_view(), name='home'),
	url(r'^create/$', CreateTeamView.as_view(), name='create'),
	url(r'^(?P<team_id>-?\d+)/$', TeamView.as_view(), name='team'),
	url(r'^delete/(?P<team_id>-?\d+)/$', TeamDeleteView.as_view(), name='deleteTeam'),
]
