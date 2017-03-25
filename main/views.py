from django.shortcuts import render
from django.http import HttpResponse
from main.models import user , hostsong , djsessions , finalplaylist
import json,requests
# Create your views here.

def song(request, foo):
	# a = user.objects.all()
	a = finalplaylist.objects.all().filter(hostedsession=foo)[0]
	return HttpResponse(a.hostname)

