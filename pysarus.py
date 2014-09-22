#Pysarus
#A python wrapper for Big Huge Thesarus
#Jacob Adams

import urllib.request
import json

#where to save reteived defintions
#if None than no files are saved
savepath = "."

#Your API key for Big Huge Thesarus
APIkey = ""

def dict(word):
	if(savepath):
		try:
			return json.load(savepath+word)
		else:
			pass
