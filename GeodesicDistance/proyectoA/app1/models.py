from __future__ import unicode_literals
from django.forms import ModelForm
from django.db import models
from django.contrib.gis.db import models

# Create your models here.



class ponto1(models.Model):

    nome = models.CharField(max_length=200)
    nome2 = models.CharField(max_length=200)
    ponto1  = models.PointField(srid=4326)
    ponto2  = models.PointField(srid=4326)
    d = models.CharField(max_length=200)


    def __unicode__(self):
    	return self.nome


class ponto1Form(ModelForm):
    class Meta:
        model = ponto1
        fields = '__all__'