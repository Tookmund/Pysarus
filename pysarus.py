#!/usr/bin/python3
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

def thesarus(word):
	if(savepath):
		try:
			return json.load(savepath+word)
		except:
			print("No file found in "+savepath+" for "+word)
		web = urllib.request.urlopen("http://words.bighugelabs.com/api/2/"+word+"/json")
		jsonobj = json.loads(web.read())
		if(savepath):
			json.dump(jsonobj,savepath+word)
		return jsonobj
