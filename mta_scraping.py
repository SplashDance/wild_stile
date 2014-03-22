# Scraping the site: http://www.mta.info/developers/turnstile.html

import urllib2
from bs4 import BeautifulSoup


data_path = ("/Applications/Python 2.7/Python Files/Udacity/Courses/"
	"Intro to Data Science/MTA Data/scraping_turnstile_data/")
site = "http://www.mta.info/developers/"

mta = BeautifulSoup(urllib2.urlopen(site + "turnstile.html").read())
turnstile_links = []

for link in mta.find_all('a'):
	data = link.get('href')
	if data and 'data' in data:
		turnstile_links.append(data)


for data in turnstile_links:
	name = data.split("/")
	with open(data_path + name[-1], 'w+') as tmp:
		data_string = urllib2.urlopen(site + data).read()
		tmp.write(data_string)

print "Finished Scraping!"




