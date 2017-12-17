from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.http import HttpResponse

urlpatterns = [
    url(r'^mapa/$', views.index, name='index'),
    
]