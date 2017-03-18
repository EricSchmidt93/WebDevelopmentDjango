#!/usr/bin/env python
#  -*- coding: UTF-8 -*-
# vim: set fileencoding=UTF-8 :

from django.views.generic import TemplateView, DetailView, CreateView, DeleteView
from .models import *
from members.models import Member
from django.core.urlresolvers import reverse_lazy


class HomeView(DetailView):

	"""
	Teamliste
	"""
	template_name = "team/home.html"
	model = Team
	context_object_name = "teams"
	
	def get_object(self):
		return Team.objects.all()

		
class CreateTeamView(CreateView):

	"""
	Team erstellen
	"""
	template_name = "team/create.html"
	model = Team
	success_url = reverse_lazy('teams:home')
	fields = ['name', 'topic']
		
	
class TeamView(DetailView):

	"""
	Teamseite
	"""
	template_name = "team/team.html"
	model = Team
	context_object_name = "team"
	
	def get_object(self):
		return Team.objects.get(pk = self.kwargs['team_id'])
		
	def get_context_data(self, **kwargs):
		context = super(TeamView, self).get_context_data(**kwargs)
		
		context['teamMembers'] = Member.objects.filter(team = self.kwargs['team_id'])
		
		return context
	
	
class TeamDeleteView(DeleteView):

	"""
	Team löschen
	"""
	success_url = reverse_lazy('teams:home')
	model = Team

	def get_object(self):
		# delete all members of this team
		Member.objects.filter(team = self.kwargs['team_id']).delete()
	
		return Team.objects.get(pk = self.kwargs['team_id'])