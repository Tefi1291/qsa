# -*- coding: utf-8 -*-
from django.forms import forms
from django.forms import ModelForm
from series.models import *


class SeriesForm(ModelForm):

    class Meta:
        model = Series



