#!/usr/bin/env python
#  -*- coding: UTF-8 -*-
# vim: set fileencoding=UTF-8 :

from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=30)
    topic = models.CharField(max_length=30)