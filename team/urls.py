#!/usr/bin/env python
#  -*- coding: UTF-8 -*-
# vim: set fileencoding=UTF-8 :

from django.conf.urls import url

from .views import HomeView

urlpatterns = [
	url(r'^$', HomeView.as_view(), name='home'),
]
