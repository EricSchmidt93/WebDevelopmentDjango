#!/usr/bin/env python
#  -*- coding: UTF-8 -*-
# vim: set fileencoding=UTF-8 :

from django.conf.urls import url

from .views import *

urlpatterns = [
	url(r'^create/$', MemberCreateView.as_view(), name='create'),
	url(r'^delete/(?P<member_id>-?\d+)/$', MemberDeleteView.as_view(), name='deleteMember'),
]