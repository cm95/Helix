#calculates btc received in wallet 
import codecs
import sys 
import requests

#add wallets here 
files = ['old20.html', 'old19.html', 'old18.html', 'old17.html', 'old16.html', 'old15.html', 'old14.html', 'old13.html', 'old12.html', 'old11.html', 'old10.html', 'old9.html', 'old8.html', 'old7.html', 'old6.html', 'old5.html', 'old4.html', 'old3.html', 'old2.html']
for f in files:
	codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)
	with open(f, 'r') as myfile:
		data=myfile.read().replace('\n', '')

	result = data.split()
	import re
	def findIndexes(regex):
		regex=re.compile(regex)
		locs, matches = zip(*[(idx, string) for idx, string in enumerate(result) if re.match(regex, string)])
		return locs
		
	number_list = []
	#+ = received 
	pluslocs = findIndexes('\+')


	alist = []
	for j in pluslocs:
		#print result[j]
		alist.append(result[j])
		
	l = []
	for t in alist:
		try:
			l.append(float(t))
			number_list.append(float(t))
		except ValueError:
			pass
		
		
	s = sum(l)
	print(str(s)) 

