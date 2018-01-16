import json
import urllib.request

def all(low=False):
	response=urllib.request.urlopen("http://www.bestemmie.org/api/bestemmie/?format=json").read()
	js=json.loads(response)
	bestemmie =[]
	for j in js:
		if low:
			bestemmie.append(j['bestemmia_low'])
		else:
			bestemmie.append(j['bestemmia_upp'])
	return bestemmie

def bestemmia(low=False):
	response=urllib.request.urlopen("http://www.bestemmie.org/api/bestemmie/random?format=json").read()
	js=json.loads(response)
	for j in js:
		if low:
			return j['bestemmia_low']
		else:
			return j['bestemmia_upp']

def bestemmia_id(id):
	response=urllib.request.urlopen("http://www.bestemmie.org/api/bestemmie/"+str(id)+"?format=json").read()
	js=json.loads(response)
	return js['bestemmia']
	
		
