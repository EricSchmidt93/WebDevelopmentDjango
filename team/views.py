#!/usr/bin/env python
#  -*- coding: UTF-8 -*-
# vim: set fileencoding=UTF-8 :

from django.views.generic import TemplateView, DetailView, CreateView, DeleteView
from .models import *
from django.core.urlresolvers import reverse_lazy


class HomeView(TemplateView):

    """
    Dummy
    """
    template_name = "team/home.html"

        
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
    
	
class TeamDeleteView(DeleteView):
	"""
	Team löschen
	"""
	template_name = "team/confirm_delete.html"
	success_url = reverse_lazy('teams:home')
	model = Team
	def get_object(self):
		return Team.objects.get(pk = self.kwargs['team_id'])
    
	# bypass django allowing only post to delete directly, never ever do this in production
	#def get(self, *args, **kwargs):
	#	return self.post(*args, **kwargs)