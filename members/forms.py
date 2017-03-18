#!/usr/bin/env python
#  -*- coding: UTF-8 -*-
# vim: set fileencoding=UTF-8 :

from django import forms
from .models import *
import re


class MemberCreationForm(forms.ModelForm):

	"""
	Form zur Mitgliedserstellung
	"""
	
	
	class Meta:
		model = Member
		fields = ('name', 'short', 'team')
		
	def clean(self):
		cleaned_data = super(MemberCreationForm, self).clean()
		
		short = cleaned_data.get('short')
		
		r = re.compile('[a-z]{2}\d{3}')
		if not r.match(short):
			self._errors['short'] = self.error_class(['Please enter a valid string!'])
		
		return cleaned_data