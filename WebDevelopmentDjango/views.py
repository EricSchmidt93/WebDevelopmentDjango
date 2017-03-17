#!/usr/bin/env python
#  -*- coding: UTF-8 -*-
# vim: set fileencoding=UTF-8 :

from django.views.generic import TemplateView
import datetime


class MainView(TemplateView):

	"""
	Startseite der Webanwendung
	"""
	template_name = "home.html"
	
	def get_context_data(self, **kwargs):
		context = super(MainView, self).get_context_data(**kwargs)
		
		context['today'] = datetime.date.today()
		
		return context