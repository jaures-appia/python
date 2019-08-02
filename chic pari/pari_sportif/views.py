from django.shortcuts import render
from .scrap import *

def index(request):
	nbre = nbrDirect()
	data = scrapFoot()
	return render(request, 'index.html', {'result' : data, 'nbre' : nbre})

def base(request):
	nbre = nbrDirect()
	return render(request, 'base.html', {'nbre' : nbre})