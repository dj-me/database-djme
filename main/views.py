from django.shortcuts import render
from django.http import HttpResponse
from main.models import user , hostsong , djsessions , finalplaylist
import json,requests
from django.db.models import Count
# Create your views here.

def song(request, foo):
	aa = djsessions.objects.all().filter(hostedsession=foo)
	songSorted = hostsong.objects.all().filter(hostedsession=aa).order_by('counter')
	return HttpResponse(songSorted)

