# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import*
# Register your models here.


class ponto1Admin(LeafletGeoAdmin):
	list_display=('nome','ponto1', 'ponto2','nome2')



admin.site.register(ponto1 , ponto1Admin)