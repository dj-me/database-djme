from django.shortcuts import render
from django.http import HttpResponse
from main.models import user , hostsong , djsessions , finalplaylist
import json,requests
from django.db.models import Count
# Create your views here.

def song(request, foo):
	aa = djsessions.objects.all().filter(hostedsession=foo)
	songSorted = hostsong.objects.all().filter(hostedsession=aa).order_by('counter')
	finalList = songSorted.reverse()
	# print finalList
	# return HttpResponse(finalList)
	array = []
	for item in finalList:
		array.append(item.song)

	# return HttpResponse(finalList)
	context_dict = {}
	context_dict['array'] = array
	return render(request,'main/nava-radio-home.html',context_dict)
