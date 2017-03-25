from django.shortcuts import render
from django.http import HttpResponse
from main.models import user , hostsong
import json,requests
# Create your views here.

def song(request):
	return HttpResponse("hy")

