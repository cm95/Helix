import numpy as np
from bs4 import BeautifulSoup
import urllib2
import decimal

#blockchain.info, find output *manually enter if >1 output 
transaction = "https://blockchain.info/tx/0bd33dba517cccd7ea3f0b6c53a5eadd983529d61d25ec50c8b54508574cb838"

web = urllib2.urlopen(transaction).read()  #whole page 
soup = BeautifulSoup(web, "html.parser")
table = soup.findAll('table' ,attrs={'class':'table table-striped'})
table = table[2]
first_td = table.findAll('td')
first_td = first_td[3] 
text = first_td.renderContents()
trimmed_text = text.strip()
split = trimmed_text.split()
split =  split[2]
chosen = [str(x) for x in split.split(">")]
output =  float(chosen[1])
print output

#Find block number  
web = urllib2.urlopen(transaction).read()  #whole page 
soup = BeautifulSoup(web, "html.parser")
table = soup.findAll('table' ,attrs={'class':'table table-striped'})
table = table[1]
first_td = table.findAll('tr')
first_td = first_td[3] 
text = first_td.renderContents()
trimmed_text = text.strip()
split = trimmed_text.split()
split =  split[5]
last = [str(x) for x in split.split(">")]
last = last[1]
last = [str(x) for x in last.split("<")]
blockNumber =  int(last[0])
print blockNumber

#create a list of numbers that will be used in search 
list = np.arange(0.9749999312,0.9793780897,0.000001)

#range of blocks searched 
range = range(2,6)

#search blocks for value 
for a in range: 
	be = blockNumber + a
	#open webpage, get table 
	web = urllib2.urlopen("https://blockchain.info/search?search=" + str(be)).read()  #whole page 
	soup = BeautifulSoup(web, "html.parser")
	table = soup.findAll("table", {'class':'table table-striped'}) #Correct table 

	#Go through all numbers created; check if found; print found 
	for i in list: 
		j = str(round((i * output),7))
		d = decimal.Decimal(j)
		if d.as_tuple().exponent <= -6:
			for line in table: #if you see a line in the table
				if line.get_text().find(str(d)) > -1 : #and you find the specific string
					ff = open(r"C:\python27\block1.html", "a")
					line.prettify().encode("utf-8") #print it
					ff.write(str(line))
					ff.write(j)
					ff.write("\n")
					ff.close()
					
#delete duplicate lines 
lines_seen = set() # holds lines already seen
outfile = open(r"C:\python27\block2.html", "w")
for line in open(r"C:\python27\block1.html", "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()	