#!/usr/bin/env python
#  -*- coding: UTF-8 -*-
# vim: set fileencoding=UTF-8 :

from django.db import models
from team.models import *


class Member(models.Model):
	name = models.CharField(max_length=30)
	short = models.CharField(max_length=5)
	
	team = models.ForeignKey(Team)