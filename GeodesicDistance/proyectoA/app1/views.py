from __future__ import unicode_literals

from django.shortcuts import render

import json
from geopy.distance import distance as geopy_distance
from django.http import HttpResponse
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.utils.timesince import timesince
from django.views.decorators.cache import cache_page
from app1.models import*
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.contrib.gis.geos import fromstr


@method_decorator(csrf_exempt,name='dispatch')
@cache_page(60 * 15)
@csrf_exempt

def ponto_1(request):

    if request.method=='POST':
		ulat1=request.POST.get("latitude1")
		unome=request.POST.get("nome1")
		unome2 = request.POST.get("nome2")
		ulng1=request.POST.get("longitude1")
		coord1=fromstr('POINT(%s %s )' % (ulng1,ulat1),srid=4326)
		ulat2=request.POST.get("latitude2")
		ulng2=request.POST.get("longitude2")
		coord2=fromstr('POINT(%s %s )' % (ulng2,ulat2),srid=4326)
		ud = geopy_distance(coord1,coord2)
		novo1=ponto1(nome=unome,ponto1=coord1, ponto2=coord2, nome2=unome2, d = ud)
		novo1.save()

		d = geopy_distance(coord1,coord2)
		print d.meters
		return render_to_response('ponto_1.html') 
    else:
	    HttpResponse("ERRO")	

@method_decorator(csrf_exempt,name='dispatch')
@cache_page(60 * 15)
@csrf_exempt

def index(request):
    
    return render_to_response('index.html')

@csrf_exempt
def show(request):
	context={'product_list': ponto1.objects.all()}
	return render(request,'show.html',context)

