from django.shortcuts import render
from django.http import HttpResponse
from .donnees import *


# Create your views here.

def bonjour(request):
	return render(request, "pari/home.html")

def inscription(request):
	nbre = nbrDirect()
	return render(request, "pari/inscription.html", {'nbre' : nbre})

def connection(request):
	nbre = nbrDirect()
	return render(request, "pari/connection.html", {'nbre' : nbre})

def pariez(request):
	nbre = nbrDirect()
	return render(request, "pari/pariez.html", {'nbre' : nbre})

def direct(request):
	nbre = nbrDirect()
	scrap = scrapDirect()
	return render(request, "pari/direct.html", {'result' : scrap, 'nbre' : nbre})

def hier(request):
	nbre = nbrDirect()
	urlhier = scrapUrl() 
	lien = urlhier['hier']
	donnees = scrapFootHier(lien)
	return render(request, "pari/match_hier.html", {'result' : donnees, 'nbre' : nbre})

def demain(request):
	nbre = nbrDirect()
	urldemain = scrapUrl() 
	lien = urldemain['demain']
	donnees = scrapFootDemain(lien)
	return render(request, "pari/match_demain.html", {'result' : donnees, 'nbre' : nbre})
