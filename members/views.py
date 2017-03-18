#!/usr/bin/env python
#  -*- coding: UTF-8 -*-
# vim: set fileencoding=UTF-8 :

from django.views.generic import TemplateView, CreateView, DeleteView
from .models import *
from .forms import *
from django.core.urlresolvers import reverse_lazy

		
class MemberCreateView(CreateView):

	"""
	Mitglied hinzufügen
	"""
	template_name = "members/create.html"
	form_class = MemberCreationForm
	model = Member
	success_url = reverse_lazy('teams:home')

	
class MemberDeleteView(DeleteView):

	"""
	Mitglied löschen
	"""
	success_url = reverse_lazy('teams:home')
	model = Member
	
	def get_object(self):
		return Member.objects.get(pk = self.kwargs['member_id'])