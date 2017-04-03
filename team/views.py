#!/usr/bin/env python
#  -*- coding: UTF-8 -*-
# vim: set fileencoding=UTF-8 :

from django.views.generic import TemplateView, DetailView, CreateView
from .models import *
from django.core.urlresolvers import reverse_lazy


class HomeView(TemplateView):

    """
    Dummy
    """
    template_name = "team/home.html"