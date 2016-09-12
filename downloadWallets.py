from bs4 import BeautifulSoup
import urllib2
import urllib
import time
from datetime import datetime
start_time = datetime.now()
#wallet location wallerexplorer
wallet = "https://www.walletexplorer.com/wallet/HelixMixer"

#Find last wallet page number  
web = urllib2.urlopen(wallet).read()  #whole page 
soup = BeautifulSoup(web, "html.parser")
table = soup.findAll('div' ,attrs={'class':'paging'})
ja = table[1]
list =[]
for line in ja: 
	list.append(line)
line =  list[1]
line1 = line.split()
last = int(line1[3])

#wallet to download 
my_array = range(1,last + 1)
for i in my_array:
	i +1
	web = urllib.urlopen(wallet + "?page=" + str(i)).read()
	soup = BeautifulSoup(web, "lxml")
	s = soup.prettify().encode("utf-8")
	ff = open(r"C:\python27\test.html", "a")
	ff.write(s)
	ff.close()
	time.sleep(2) #prevent lockout 
print "completed "

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))	