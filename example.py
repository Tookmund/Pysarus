import pysarus

syn = "syn"
ant = "ant"

word = "word"
jsonobj = pysarus.thesarus("word")
for type in ["noun","verb","adjective","adverb"]:
	print(type+" synonyms for "+word+" include")
	for x in jsonobj.noun.syn:
		print(x)
		
	print(type+" antonyms for "+word+" include")
	for x in jsonobj.type.ant:
		print(x)
